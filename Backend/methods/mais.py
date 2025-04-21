import pandas as pd
import numpy as np
from scipy.special import softmax
from methods.gan import train_gan, generate_data_from_gan
from methods.graphe import *

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

    # Génération des graphes nécessaires pour tous les paramètres
    df_base, df_generated = charger_Fichier("csv", 'data/maïs.csv', 'data_genere/maïs_generated.csv')
    params = ['water req', 'Min Temp', 'Max Temp', 'Humidity', 'Wind', 'Sun', 'Rad', 'altitude', 'latitude', 'longitude']
    '''for param in params:
         representer_selon_mois_histogramme(param, 'mais', df_base, df_generated)
         representer_selon_mois_boxplot(param, 'mais', df_base, df_generated)
         plot_cumulative_frequency(param, 'mais', df_base, df_generated)'''


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

def mais_train(chemin_lecture, latent_dim, epochs, batch_size, sample_interval, culture):
    cat_variables = ['month', 'city', 'crop', 'soil']
    COLS_USED = ['water req', 'month', 'Min Temp', 'Max Temp', 'Humidity', 'Wind', 'Sun', 'Rad','rain', 'altitude', 'latitude', 'longitude', 'crop', 'soil', 'city']
    df = pd.read_excel(chemin_lecture, engine='openpyxl')
    data_augmentation_train(df, latent_dim, epochs, batch_size, sample_interval, COLS_USED, cat_variables, culture)

def mais_generator(chemin_sortie, num_samples, culture):
    city_cols = ['city_chennai', 'city_delhi', 'city_jaipur', 'city_kolkata', 'city_kurnool']
    month_cols = ['month_January', 'month_February', 'month_November', 'month_December', 'month_October']
    months_list = ['January','February', 'November', 'December','October']
    soil_cols = ['soil_red lomy sand']
    crops_cols = ['crop_maize']
    generated_df = data_augmentation(num_samples, culture)
    after_generation(generated_df, city_cols, month_cols, crops_cols, soil_cols,  chemin_sortie, months_list)


