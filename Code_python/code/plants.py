import pandas as pd
import numpy as np
from scipy.special import softmax
from gan import train_gan, generate_data_from_gan
from graphe import *

def clean_month_column(df):
    # Dictionnaire de correspondance entre les noms des mois et leurs numéros
    month_mapping = {
        'January': 1,
        'january': 1,
        'February': 2,
        'february': 2,
        'March': 3,
        'march': 3,
        'April': 4,
        'april': 4,
        'May': 5,
        'may': 5,
        'June': 6,
        'june': 6,
        'July': 7,
        'july': 7,
        'August': 8,
        'august': 8,
        'September': 9,
        'september': 9,
        'October': 10,
        'october': 10,
        'November': 11,
        'november': 11,
        'December': 12,
        'december': 12
    }

    # Remplacer les noms des mois par leurs numéros correspondants
    df['month'] = df['month'].map(month_mapping)

    # Remplacer les valeurs non-finites par une valeur par défaut (par exemple 0)
    df['month'] = df['month'].fillna(0)

    # Convertir les valeurs de la colonne 'month' en entiers
    df['month'] = df['month'].astype(int)

    # Remplacer les valeurs nulles dans la colonne 'month' par la valeur la plus fréquente à part 0
    mode_value = df['month'][df['month'] != 0].mode()[0]

    # Remplacer les valeurs nulles dans la colonne 'month' par la valeur la plus fréquente
    df['month'] = df['month'].replace(0, mode_value)

    # Dictionnaire de correspondance entre les numéros des mois et leurs noms
    month_mapping = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    # Remplacer les numéros des mois par leurs noms correspondants
    df['month'] = df['month'].map(month_mapping)

    return df

def clean_numerical_column(df,numerical_columns):
    # Pour chaque colonne numérique
    for col in numerical_columns:
        # Remplacer les valeurs non-finites par une valeur par défaut (par exemple 0)
        df[col] = df[col].fillna(0)
        
        # Calculer la valeur la plus fréquente à l'exception de zéro
        mode_value = df[df[col] != 0][col].mode().iloc[0]
        
        # Remplacer les valeurs nulles dans la colonne par la valeur la plus fréquente du mois
        df[col] = df[col].replace(0, mode_value)
    
    return df

def clean_data(df):
    df = df[df['longitude'] != 'wheat']
    df = df.drop_duplicates()
    df = clean_month_column(df)
    # Liste des colonnes numériques à nettoyer
    numerical_columns = ['water req', 'Min Temp', 'Max Temp', 'Humidity', 'Wind', 'Sun', 'Rad', 'Rain', 'altitude', 'latitude', 'longitude'] 
    df = clean_numerical_column(df,numerical_columns)
    df['crop'] = df['crop'].str.strip().replace('rice ', 'rice')

    crops = ['potato', 'rice']
    soils = {'potato': 'red loamy', 'rice': 'BLACK CLAY'}

    # Initialiser un compteur pour suivre l'index de la culture à utiliser
    crop_index = 0

    # Parcourir les lignes du DataFrame
    for index, row in df.iterrows():
        # Vérifier si la valeur de 'crop' est NaN
        if pd.isna(row['crop']):
            # Remplacer NaN par la culture actuelle
            df.at[index, 'crop'] = crops[crop_index]
            # Mettre à jour l'index de la culture pour la prochaine itération
            crop_index = (crop_index + 1) % len(crops)  # Alterne entre 0 et 1 pour les index de cultures
            # Mettre à jour le type de sol en fonction de la culture
            df.at[index, 'soil'] = soils[df.at[index, 'crop']]

    # Définir les villes correspondant à chaque culture
    cities_potato = ['jaipur', 'kolkata', 'mumbai', 'delhi']
    cities_rice = ['chennai', 'kurnool']

    # Créer des colonnes pour chaque ville avec des valeurs NaN
    for city in cities_potato + cities_rice:
        df[city] = np.nan

    # Initialiser un compteur pour suivre l'index de la ville à utiliser
    city_index = 0

    # Parcourir les lignes du DataFrame
    for index, row in df.iterrows():
        # Vérifier si la valeur de 'city' est NaN
        if pd.isna(row['city']):
            # Déterminer la culture de la ligne actuelle
            current_crop = row['crop']
            # Remplacer NaN par la ville correspondant à la culture actuelle
            if current_crop == 'potato':
                df.at[index, cities_potato[city_index % len(cities_potato)]] = 1
            elif current_crop == 'rice':
                df.at[index, cities_rice[city_index % len(cities_rice)]] = 1
            # Mettre à jour l'index de la ville pour la prochaine itération
            city_index += 1
    return df

# Fonction pour extraire le mois à partir des colonnes month_*
def extract_month(row, months_list):
    for month in months_list:
        if row[f'month_{month}']:
            return month
    return None

def after_generation(generated_df, city_cols, month_cols, crops_cols, soil_cols,  chemin_sortie, months_list):
    # Appliquer softmax pour convertir les scores des villes en probabilités
    city_scores = generated_df[city_cols].values  # Extraire les scores des villes dans un array numpy
    city_probabilities = softmax(city_scores, axis=1)

    # Sélectionnez la ville avec la probabilité la plus élevée pour chaque ligne
    max_city_indices = np.argmax(city_probabilities, axis=1)

    generated_df['city'] = [city_cols[i].split('_')[1] for i in max_city_indices]

    # Suppression des anciennes colonnes de villes
    generated_df.drop(columns=city_cols, inplace=True)

    # Soil
    soil_scores = generated_df[soil_cols].values  # Extraire les scores des soil dans un array numpy
    soil_probabilities = softmax(soil_scores, axis=1)

    # Sélectionnez la soil avec la probabilité la plus élevée pour chaque ligne
    max_soil_indices = np.argmax(soil_probabilities, axis=1)

    generated_df['soil'] = [soil_cols[i].split('_')[1] for i in max_soil_indices]

    # Suppression des anciennes colonnes de soil
    generated_df.drop(columns=soil_cols, inplace=True)

    # Crops
    # Appliquer softmax pour convertir les scores des crops en probabilités
    crops_scores = generated_df[crops_cols].values  # Extraire les scores des soil dans un array numpy
    crops_probabilities = softmax(crops_scores, axis=1)

    # Sélectionnez la crops avec la probabilité la plus élevée pour chaque ligne
    max_crops_indices = np.argmax(crops_probabilities, axis=1)

    generated_df['crops'] = [crops_cols[i].split('_')[1] for i in max_crops_indices]

    # Suppression des anciennes colonnes de crops
    generated_df.drop(columns=crops_cols, inplace=True)
    # Génération des graphes nécessaires pour tous les paramètres
    df_base, df_generated = charger_Fichier("csv", 'data/data_plants.csv', 'data_genere/data_plants_generated.csv')
    params = ['water req', 'Min Temp', 'Max Temp', 'Humidity', 'Wind', 'Sun', 'Rad', 'Rain', 'altitude', 'latitude', 'longitude']
    '''for param in params:
         representer_selon_mois_histogramme(param, 'plants', df_base, df_generated)
         representer_selon_mois_boxplot(param, 'plants', df_base, df_generated)
         plot_cumulative_frequency(param, 'plants', df_base, df_generated)'''


    # Appliquer softmax pour convertir les scores des mois en probabilités
    month_scores = generated_df[month_cols].values  # Extraire les scores des mois dans un array numpy
    month_probabilities = softmax(month_scores, axis=1)

    # Sélectionnez le mois avec la probabilité la plus élevée pour chaque ligne
    max_month_indices = np.argmax(month_probabilities, axis=1)

    # Remplacer les valeurs de mois par True/False en fonction de l'indice maximum
    for i, col_index in enumerate(max_month_indices):
        for j, _ in enumerate(month_cols):
            generated_df.at[i, month_cols[j]] = (j == col_index)

    # Correction postérieure pour garantir True/False plutôt que 1/0
    generated_df[month_cols] = generated_df[month_cols].astype(bool)

    # Appliquer la fonction sur chaque ligne pour créer une nouvelle colonne 'month'
    generated_df['month'] = generated_df.apply(lambda row: extract_month(row, months_list), axis=1)

    # Supprimer les colonnes spécifiées
    generated_df.drop(columns=month_cols, inplace=True)

    # Sauvegarder le DataFrame modifié dans un fichier CSV
    generated_df.to_csv(chemin_sortie, index=False)

def data_augmentation_train(df, latent_dim, epochs, batch_size, sample_interval, COLS_USED, cat_variables, culture):
    df = df[COLS_USED]
    # Convertir les variables catégorielles 
    # Boucle sur chaque variable catégorielle
    for cat_variable in cat_variables:
        df = pd.get_dummies(df, columns=[cat_variable])

    # Appel au générateur GAN de données
    train_gan(df, latent_dim, epochs, batch_size, sample_interval, culture)

def data_augmentation(num_samples, culture):
    generated_df = generate_data_from_gan(num_samples, culture)
    return generated_df

def plants_train(chemin_lecture, latent_dim, epochs, batch_size, sample_interval, culture):
    cat_variables = ['month', 'city', 'soil', 'crop']
    COLS_USED = ['water req', 'month', 'Min Temp', 'Max Temp', 'Humidity', 'Wind', 'Sun', 'Rad', 'Rain', 'altitude', 'latitude', 'longitude', 'crop', 'soil', 'city']
    df = pd.read_csv(chemin_lecture)
    df = clean_data(df)
    df['longitude'] = df['longitude'].astype(float)
    data_augmentation_train(df, latent_dim, epochs, batch_size, sample_interval, COLS_USED, cat_variables, culture)

def plants_generator(chemin_sortie, num_samples, culture):
    city_cols = ['city_chennai', 'city_delhi', 'city_jaipur', 'city_kolkata', 'city_kurnool', 'city_mumbai']
    soil_cols = ['soil_BLACK CLAY', 'soil_red loamy']
    crops_cols = ['crop_potato', 'crop_rice']
    month_cols = ['month_April', 'month_August', 'month_July', 'month_June', 'month_March', 'month_May', 'month_September']
    months_list = ['April', 'July', 'June', 'March', 'May','September', 'August']
    generated_df = data_augmentation(num_samples, culture)
    after_generation(generated_df, city_cols, month_cols, crops_cols, soil_cols,  chemin_sortie, months_list)


# Entrainement des données
train_nb = 100
plants_train('./data/data_plants.csv', 100, train_nb, 32, 100, 'plants')

# Géneration des données
plants_generator('./data/data_plants_generated.csv', 40, 'plants')