import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from keras.models import Sequential, Model, load_model
from keras.layers import Dense, LeakyReLU, BatchNormalization, Input
from keras.optimizers import Adam
from keras.initializers import RandomNormal
import pickle
from methods.graphe import *

# Fonction pour remplacer par la moyenne des intervalles
def replace_with_interval_mean(value):
    min_val, max_val = map(int, value.split('-'))
    return str((min_val + max_val) // 2)

# Construction de generateur
def build_generator(latent_dim, output_dim):
    init = RandomNormal(stddev=0.02)
    model = Sequential([
        Dense(128, input_dim=latent_dim, kernel_initializer=init),
        LeakyReLU(alpha=0.2),
        BatchNormalization(momentum=0.8),
        Dense(256, kernel_initializer=init),
        LeakyReLU(alpha=0.2),
        BatchNormalization(momentum=0.8),
        Dense(512, kernel_initializer=init),
        LeakyReLU(alpha=0.2),
        BatchNormalization(momentum=0.8),
        Dense(output_dim, activation='tanh', kernel_initializer=init)
    ])
    return model

# Construction de discriminateur
def build_discriminator(input_dim):
    init = RandomNormal(stddev=0.02)
    model = Sequential([
        Dense(512, input_dim=input_dim, kernel_initializer=init),
        LeakyReLU(alpha=0.2),
        Dense(256, kernel_initializer=init),
        LeakyReLU(alpha=0.2),
        Dense(1, activation='sigmoid', kernel_initializer=init)
    ])
    model.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5), metrics=['accuracy'])
    return model

def split_range_to_min_max(df, column_name, new_column_prefix):
    df[[f'{new_column_prefix}_min', f'{new_column_prefix}_max']] = df[column_name].str.split('-', expand=True).astype(float)
    return df.drop(columns=[column_name])

def clean_df(df):
    # Étape 1: Gérer les plages de valeurs
    # Appliquer la fonction aux colonnes concernées
    df = split_range_to_min_max(df, 'Total growing period (days)', 'Growing_period_days')
    df = split_range_to_min_max(df, 'Crop water need (mm/total growing period)', 'Crop_water_need_mm')

    # Étape 2: Vérifier et traiter les valeurs manquantes
    # Remplacer les valeurs manquantes par la moyenne pour les colonnes 'Crop_water_need_mm_min' et 'Crop_water_need_mm_max'
    df['Crop_water_need_mm_min'].fillna(df['Crop_water_need_mm_min'].mean(), inplace=True)
    df['Crop_water_need_mm_max'].fillna(df['Crop_water_need_mm_max'].mean(), inplace=True)
    
    
    num_columns = ['Growing_period_days_min', 'Growing_period_days_max', 'Crop_water_need_mm_min', 'Crop_water_need_mm_max']
    
    # Créer df_comparative
    df_comparative = df.copy()
    df_comparative['Growing_period_days'] = (df['Growing_period_days_max'] + df['Growing_period_days_min']) / 2
    df_comparative['Crop_water_need_mm'] = (df['Crop_water_need_mm_max'] + df['Crop_water_need_mm_min']) / 2
    df_comparative.drop(columns=num_columns, inplace=True)
    
    # Sauvegarder df_comparative dans un fichier CSV
    df_comparative.to_csv('data_genere/website_initiale_comparative.csv', index=False)
    

    # Étape 3: Normaliser les valeurs numériques
    scaler = MinMaxScaler(feature_range=(-1, 1))
    df[num_columns] = scaler.fit_transform(df[num_columns])

    #Étape 4: Convertir les variables qualitatives en valeurs numériques
    label_encoder = LabelEncoder()
    df['Crop_Code'] = label_encoder.fit_transform(df['Crop'])

    # Créer un dictionnaire de correspondance entre les codes et les noms de culture
    crop_code_mapping = dict(zip(df['Crop_Code'], df['Crop']))

    # Déplacer la colonne Crop_Code au début du DataFrame
    column_order = ['Crop_Code'] + [col for col in df.columns if col != 'Crop_Code']
    df = df[column_order]

    # Supprimer la colonne Crop
    df.drop(columns=['Crop'], inplace=True)
    
    return df, crop_code_mapping, num_columns, scaler

def train_gan(chemin_lecture, latent_dim, epochs, batch_size, sample_interval, culture):
    df = pd.read_excel(chemin_lecture)
    df, crop_code_mapping, num_cols, scaler  = clean_df(df)
    data_dim = df.shape[1] - 1  # Dimension des données d'entrée (-1 pour exclure la colonne cible)
    generator = build_generator(latent_dim, data_dim)
    discriminator = build_discriminator(data_dim)

    # Créer le modèle combiné (GAN)
    discriminator.trainable = False
    z = Input(shape=(latent_dim,))
    generated_data = generator(z)
    validity = discriminator(generated_data)

    combined = Model(z, validity)
    combined.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5))

    for epoch in range(epochs):
        # Entraîner le discriminateur
        idx = np.random.randint(0, df.shape[0], batch_size)
        real_samples = df.iloc[idx, :-1].values  # Exclure la colonne des codes des cultures
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        generated_samples = generator.predict(noise)
        d_loss_real = discriminator.train_on_batch(real_samples, np.ones((batch_size, 1)))
        d_loss_fake = discriminator.train_on_batch(generated_samples, np.zeros((batch_size, 1)))
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
        
        # Entraîner le générateur
        noise = np.random.normal(0, 1, (batch_size, latent_dim))
        valid_y = np.array([1] * batch_size)
        g_loss = combined.train_on_batch(noise, valid_y)
        
        if (epoch + 1) % sample_interval == 0:
            print(f"Epoch: {epoch+1}, D Loss: {d_loss[0]}, D Acc.: {100*d_loss[1]}, G Loss: {g_loss}")

    discriminator.save('GanEntraine/'+culture+'discriminator_model.h5')
    generator.save('GanEntraine/'+culture+'generator_model.h5')

    df.to_csv('GanEntraine/'+culture+'train_df.csv', index=False)

    with open('GanEntraine/'+culture+'gan_parameters.pkl', 'wb') as f:
        pickle.dump((latent_dim, num_cols, scaler, crop_code_mapping), f)

    print("Entraînement terminé. Modèles et DataFrame sauvegardés.")

def generate_data_from_gan(chemin_sortie, num_samples, culture):
    with open('GanEntraine/'+culture+'gan_parameters.pkl', 'rb') as f:
        latent_dim, num_cols, scaler, crop_code_mapping = pickle.load(f)

    generator = load_model('GanEntraine/'+culture+'generator_model.h5')

    latent_points = np.random.normal(0, 1, (num_samples, latent_dim))
    generated_samples = generator.predict(latent_points)

    generated_df = pd.DataFrame(generated_samples, columns=num_cols)
    generated_df[num_cols] = scaler.inverse_transform(generated_df[num_cols])

    valid_crop_codes = np.random.choice(list(crop_code_mapping.keys()), size=num_samples)
    generated_df['Crop_Code'] = valid_crop_codes
    generated_df['Crop_Name'] = generated_df['Crop_Code'].map(crop_code_mapping)

    generated_df[['Growing_period_days_min', 'Growing_period_days_max', 'Crop_water_need_mm_min', 'Crop_water_need_mm_max']] = generated_df[['Growing_period_days_min', 'Growing_period_days_max', 'Crop_water_need_mm_min', 'Crop_water_need_mm_max']].apply(np.floor)

    generated_df[['Growing_period_days_min', 'Growing_period_days_max', 'Crop_water_need_mm_min', 'Crop_water_need_mm_max']] = generated_df[['Growing_period_days_min', 'Growing_period_days_max', 'Crop_water_need_mm_min', 'Crop_water_need_mm_max']].astype(int)

    generated_df['Growing_period_days'] = generated_df['Growing_period_days_min'].astype(str) + '-' + generated_df['Growing_period_days_max'].astype(str)
    generated_df['Crop_water_need_mm'] = generated_df['Crop_water_need_mm_min'].astype(str) + '-' + generated_df['Crop_water_need_mm_max'].astype(str)
    
    generated_df.drop(['Growing_period_days_min', 'Growing_period_days_max', 'Crop_water_need_mm_min', 'Crop_water_need_mm_max', 'Crop_Code'], axis=1, inplace=True)

    col_order = ['Crop_Name'] + [col for col in generated_df.columns if col != 'Crop_Name']
    generated_df = generated_df[col_order]
    generated_df.to_csv(chemin_sortie, index=False)
    
    # Création d'une copie pour appliquer les modifications
    modified_df = generated_df.copy()

    # Application de la fonction pour remplacer par la moyenne des intervalles sur la copie
    modified_df['Growing_period_days'] = modified_df['Growing_period_days'].apply(replace_with_interval_mean)
    modified_df['Crop_water_need_mm'] = modified_df['Crop_water_need_mm'].apply(replace_with_interval_mean)

    # Réorganisation des colonnes dans la copie
    col_order = ['Crop_Name', 'Growing_period_days', 'Crop_water_need_mm']
    modified_df = modified_df[col_order]

    # Sauvegarde de la copie modifiée
    modified_df.to_csv('data_genere/website_generated_comprative.csv', index=False)
    # Génération des graphes nécessaires pour tous les paramètres
    df_base, df_generated = charger_Fichier("csv", 'data_genere/website_initiale_comparative.csv', 'data_genere/website_generated_comprative.csv')
    params = ['Growing_period_days', 'Crop_water_need_mm']
    '''for param in params:
         representer_selon_mois_histogramme(param, 'website', df_base, df_generated)
         representer_selon_mois_boxplot(param, 'website', df_base, df_generated)
         plot_cumulative_frequency(param, 'website', df_base, df_generated)'''
