import pandas as pd
from methods.gan import train_gan, generate_data_from_gan
from methods.graphe import *

# Fonction pour extraire le mois à partir des colonnes month_*
def extract_month(row, months_list):
    for month in months_list:
        if row[f'month_{month}']:
            return month
    return None

def after_generation(generated_df, chemin_sortie):
    # Convertir les valeurs de la colonne 'hour' en objets de temps
    generated_df['hour'] = pd.to_datetime(generated_df['hour'], unit='h').dt.strftime('%H.%M')
    generated_df.to_csv(chemin_sortie, index=False)
    # Génération des graphes nécessaires pour tous les paramètres
    df_base, df_generated = charger_Fichier("csv", 'data/tomates.csv', 'data_genere/tomates_generated.csv')
    params = ['time', 'water', 'hour']
    '''for param in params:
         # representer_selon_mois_histogramme(param, 'tomatos', df_base, df_generated)
         representer_selon_mois_boxplot(param, 'tomatos', df_base, df_generated)
         plot_cumulative_frequency(param, 'tomatos', df_base, df_generated)'''

def data_augmentation_train(df, latent_dim, epochs, batch_size, sample_interval, COLS_USED, culture):
    df = df[COLS_USED]
    # Appel au générateur GAN de données
    train_gan(df, latent_dim, epochs, batch_size, sample_interval, culture)

def data_augmentation(num_samples, culture):
    generated_df = generate_data_from_gan(num_samples, culture)
    return generated_df

def tomato_train(chemin_lecture, latent_dim, epochs, batch_size, sample_interval, culture):
    COLS_USED = ['simulation_id','time','water','hour']
    df = pd.read_csv(chemin_lecture)
    data_augmentation_train(df, latent_dim, epochs, batch_size, sample_interval, COLS_USED, culture)

def tomato_generator(chemin_sortie, num_samples, culture):
    generated_df = data_augmentation(num_samples, culture)
    after_generation(generated_df, chemin_sortie)

