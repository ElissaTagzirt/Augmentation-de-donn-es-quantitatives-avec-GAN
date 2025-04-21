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

def after_generation(generated_df, city_cols, month_cols, chemin_sortie, months_list):
    # Ajouter une colonne 'Soil' avec la valeur 'BLACK KLAY' partout
    generated_df['Soil'] = 'BLACK KLAY'

    # Ajouter une colonne 'Crop' avec la valeur 'rice' partout
    generated_df['Crop'] = 'rice'
    # Appliquer softmax pour convertir les scores des villes en probabilités
    city_scores = generated_df[city_cols].values  # Extraire les scores des villes dans un array numpy
    city_probabilities = softmax(city_scores, axis=1)

    # Sélectionnez la ville avec la probabilité la plus élevée pour chaque ligne
    max_city_indices = np.argmax(city_probabilities, axis=1)

    generated_df['CITY'] = [city_cols[i].split('_')[1] for i in max_city_indices]

    # Suppression des anciennes colonnes de villes
    generated_df.drop(columns=city_cols, inplace=True)

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
    df_base, df_generated = charger_Fichier("csv", 'data/riz.csv', 'data_genere/riz_generated.csv')
    params = ['water req', 'Min Temp', 'Max Temp', 'Humidity', 'Wind', 'Sun', 'Rad', 'rain', 'altitude', 'latitude', 'longitude']
    '''for param in params:
         representer_selon_mois_histogramme(param, 'riz', df_base, df_generated)
         representer_selon_mois_boxplot(param, 'riz', df_base, df_generated)
         plot_cumulative_frequency(param, 'riz', df_base, df_generated)'''

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

def riz_train(chemin_lecture, latent_dim, epochs, batch_size, sample_interval, culture):
    cat_variables = ['month', 'CITY']
    COLS_USED = ['water req', 'month', 'Min Temp', 'Max Temp', 'Humidity', 'Wind', 'Sun', 'Rad', 'rain', 'altitude', 'latitude', 'longitude','CITY']
    df = pd.read_csv(chemin_lecture)
    data_augmentation_train(df, latent_dim, epochs, batch_size, sample_interval, COLS_USED, cat_variables, culture)

def riz_generator(chemin_sortie, num_samples, culture):
    city_cols = ['CITY_chennai','CITY_delhi','CITY_jaipur','CITY_kolkata','CITY_kurnool','CITY_mumbai']
    month_cols = ['month_august','month_july','month_june','month_may','month_september']
    months_list = ['august','july','june','may','september']
    generated_df = data_augmentation(num_samples, culture)
    after_generation(generated_df, city_cols, month_cols, chemin_sortie, months_list)

