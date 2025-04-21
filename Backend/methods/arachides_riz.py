import pandas as pd
import numpy as np
from scipy.special import softmax
from methods.gan import train_gan, generate_data_from_gan

# Fonction pour extraire le mois à partir des colonnes month_*
def extract_month(row, months_list):
    for month in months_list:
        if row[f'month_{month}']:
            return month
    return None

def after_generation(generated_df, crop_cols, irrigation_cols, chemin_sortie):
    # Appliquer softmax pour convertir les scores des crops en probabilités
    crop_scores = generated_df[crop_cols].values  # Extraire les scores des crops dans un array numpy
    crop_probabilities = softmax(crop_scores, axis=1)

    # Sélectionnez le crop avec la probabilité la plus élevée pour chaque ligne
    max_crop_indices = np.argmax(crop_probabilities, axis=1)

    generated_df['CropType'] = [crop_cols[i].split('_')[1] for i in max_crop_indices]

    # Suppression des anciennes colonnes de crops
    generated_df.drop(columns=crop_cols, inplace=True)

    # Appliquer softmax pour convertir les scores des irrigations en probabilités
    irrigation_scores = generated_df[irrigation_cols].values  # Extraire les scores des irrigations dans un array numpy
    irrigation_probabilities = softmax(irrigation_scores, axis=1)

    # Sélectionnez l'irrigation avec la probabilité la plus élevée pour chaque ligne
    max_irrigation_indices = np.argmax(irrigation_probabilities, axis=1)

    generated_df['Irrigation(Y/N)'] = [irrigation_cols[i].split('_')[1] for i in max_irrigation_indices]

    # Suppression des anciennes colonnes de irrigation
    generated_df.drop(columns=irrigation_cols, inplace=True)

    generated_df['CropDays'] = generated_df['CropDays'].astype(int)

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

def arachides_riz_train(chemin_lecture, latent_dim, epochs, batch_size, sample_interval, culture):
    cat_variables = ['CropType','Irrigation(Y/N)']
    COLS_USED = ['CropType','CropDays','Soil Moisture','Soil Temperature','Temperature','Humidity','Irrigation(Y/N)']
    df = pd.read_excel(chemin_lecture, engine='openpyxl')
    df['CropType'] = df['CropType'].replace({1: 'riz', 2: 'arachide'})
    df['Irrigation(Y/N)'] = df['Irrigation(Y/N)'].replace({1: 'Y', 0: 'N'})
    data_augmentation_train(df, latent_dim, epochs, batch_size, sample_interval, COLS_USED, cat_variables, culture)

def arachides_riz_generator(chemin_sortie, num_samples, culture):
    crop_cols = ['CropType_arachide','CropType_riz']
    irrigation_cols = ['Irrigation(Y/N)_Y','Irrigation(Y/N)_N']
    generated_df = data_augmentation(num_samples, culture)
    after_generation(generated_df, crop_cols, irrigation_cols, chemin_sortie)


