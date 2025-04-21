import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import Dense, LeakyReLU, BatchNormalization, Input
from keras.optimizers import Adam
from keras import Model
import pickle

# Organisation et nettoyage de data et Normalisation des valeurs numériques
def pre_traitement_data(df):
    # Identifier les colonnes numériques et catégorielles
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns

    # Imputation des valeurs manquantes
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Encodage One-Hot des variables catégorielles
    df = pd.get_dummies(df, columns=cat_cols)

    # Normaliser
    scaler = MinMaxScaler(feature_range=(-1, 1))
    df[num_cols] = scaler.fit_transform(df[num_cols])

    return df, num_cols, scaler

# Construction de Générateur
def build_generator(latent_dim, data_dim):
    model = Sequential([
        # Première couche Dense: Transforme l'entrée de l'espace latent en 128 dimensions.
        Dense(128, input_dim=latent_dim),
        # Activation LeakyReLU: Introduit de la non-linéarité, permettant un petit gradient quand l'unité est inactive.
        LeakyReLU(alpha=0.2),
        # Normalisation par lots: Stabilise l'apprentissage en normalisant la sortie de la couche précédente.
        BatchNormalization(momentum=0.8),
        # Deuxième couche Dense: Augmente la dimension de l'espace à 256.
        Dense(256),
        # Activation LeakyReLU.
        LeakyReLU(alpha=0.2),
        # Normalisation par lots.
        BatchNormalization(momentum=0.8),
        # Troisième couche Dense: Étend davantage l'espace à 512 dimensions.
        Dense(512),
        # Activation LeakyReLU.
        LeakyReLU(alpha=0.2),
        # Normalisation par lots.
        BatchNormalization(momentum=0.8),
        # Dernière couche Dense: Transforme la sortie en dimension de l'espace de données réel.
        Dense(data_dim, activation='tanh')  # Utilise 'tanh' pour la sortie, normalisant les valeurs entre -1 et 1.
    ])
    return model


def build_discriminator(data_dim):
    """
    Construit le modèle du discriminateur pour un réseau GAN.

    Parameters:
    - data_dim : int
        La dimension des données d'entrée. Correspond au nombre de caractéristiques
        de l'échantillon d'entrée que le discriminateur va traiter.

    Returns:
    - model : keras.engine.sequential.Sequential
        Le modèle du discriminateur prêt à être compilé et entraîné.
    """
    # Initialisation du modèle séquentiel
    model = Sequential()

    # Ajout de la première couche dense
    # - 512 neurones
    # - 'input_dim' spécifie le nombre de caractéristiques dans l'échantillon d'entrée
    model.add(Dense(512, input_dim=data_dim))
    # Ajout d'une fonction d'activation LeakyReLU
    # - 'alpha' définit la pente de la fonction pour les valeurs négatives, permettant un petit gradient
    #   et donc, évite le problème des neurones "morts"
    model.add(LeakyReLU(alpha=0.2))

    # Ajout d'une seconde couche dense avec 256 neurones
    model.add(Dense(256))
    # Utilisation de LeakyReLU comme fonction d'activation pour introduire de la non-linéarité
    model.add(LeakyReLU(alpha=0.2))

    # Ajout d'une troisième couche dense avec 128 neurones
    model.add(Dense(128))
    # Encore une fois, utilisation de LeakyReLU pour la non-linéarité
    model.add(LeakyReLU(alpha=0.2))

    # Ajout de la couche de sortie
    # - Un seul neurone car le discriminateur effectue une tâche de classification binaire (réel vs généré)
    # - Utilisation de la fonction d'activation 'sigmoid' pour obtenir une probabilité en sortie
    model.add(Dense(1, activation='sigmoid'))

    # Le modèle est retourné et est prêt à être compilé et entraîné
    return model
# Fonction pour échantillonner des points dans l'espace latent
def sample_latent_points(latent_dim, batch_size):
    return np.random.normal(0, 1, (batch_size, latent_dim))

# Fonction pour générer des données réelles avec des labels, en s'assurant que le type est float32
def generate_real_samples(X_train,batch_size):
    idx = np.random.randint(0, X_train.shape[0], batch_size)
    real_samples = X_train[idx].astype('float32')
    real_labels = np.ones((batch_size, 1), dtype='float32')
    return real_samples, real_labels

# Fonction pour générer des données fausses avec des labels, en s'assurant que le type est float32
def generate_fake_samples(generator, latent_dim, batch_size):
    latent_points = sample_latent_points(latent_dim, batch_size).astype('float32')
    fake_samples = generator.predict(latent_points)
    fake_labels = np.zeros((batch_size, 1), dtype='float32')
    return fake_samples, fake_labels

def train_gan(df, latent_dim, epochs, batch_size, sample_interval, culture):
    # Pré-traitement des données pour s'assurer qu'elles sont dans un format approprié pour l'entraînement
    df, num_cols, scaler = pre_traitement_data(df)

    # Division des données en ensembles d'entraînement et de test, avec 20% des données comme test
    train_df, _ = train_test_split(df, test_size=0.2, random_state=42)

    # Conversion de l'ensemble d'entraînement en un tableau numpy pour faciliter le traitement par Keras
    X_train = train_df.values
    # Détermination de la dimensionnalité des données d'entrée pour configurer le discriminateur
    data_dim = X_train.shape[1]

    # Construction et compilation du discriminateur
    discriminator = build_discriminator(data_dim)
    # Utilisation de la fonction de perte 'binary_crossentropy' et de l'optimiseur Adam pour l'entraînement
    discriminator.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5), metrics=['accuracy'])

    # Construction du générateur
    generator = build_generator(latent_dim, data_dim)
    # Création d'un espace latent pour l'entrée du générateur
    z = Input(shape=(latent_dim,))
    # Génération de données à partir de l'espace latent
    generated_data = generator(z)

    # Pendant l'entraînement du modèle combiné (générateur + discriminateur), le discriminateur est non entraînable
    discriminator.trainable = False
    # Le discriminateur évalue les données générées
    validity = discriminator(generated_data)

    # Création du modèle combiné en reliant l'espace latent à la validité des données générées
    combined = Model(z, validity)
    # Compilation du modèle combiné avec la même fonction de perte et optimiseur que le discriminateur
    combined.compile(loss='binary_crossentropy', optimizer=Adam(0.0002, 0.5))

    # Boucle d'entraînement principale
    for epoch in range(epochs):
        # Génération et entraînement sur des échantillons réels
        real_samples, real_labels = generate_real_samples(X_train, batch_size)
        # Génération et entraînement sur des échantillons faux
        fake_samples, fake_labels = generate_fake_samples(generator, latent_dim, batch_size)
        
        # Entraînement du discriminateur sur les échantillons réels et faux, et calcul de la perte moyenne
        d_loss_real = discriminator.train_on_batch(real_samples, real_labels)
        d_loss_fake = discriminator.train_on_batch(fake_samples, fake_labels)
        d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
        
        # Entraînement du générateur pour améliorer sa capacité à tromper le discriminateur
        latent_points = sample_latent_points(latent_dim, batch_size)
        # Le générateur essaie de faire classer ses échantillons comme réels (label 1) par le discriminateur
        generator_labels = np.ones((batch_size, 1))
        g_loss = combined.train_on_batch(latent_points, generator_labels)
        
        # Affichage de l'état de l'entraînement à intervalles réguliers
        if (epoch + 1) % sample_interval == 0:
            print(f"Epoch {epoch + 1}, D Loss: {d_loss[0]}, D Acc: {100*d_loss[1]}, G Loss: {g_loss}")
    
    # Sauvegarde des modèles entraînés pour une utilisation future
    discriminator.save(f'GanEntraine/{culture}discriminator_model.h5')
    generator.save(f'GanEntraine/{culture}generator_model.h5')

    # Sauvegarde du DataFrame pré-traité pour référence future
    train_df.to_csv(f'GanEntraine/{culture}train_df.csv', index=False)

    # Sauvegarde des paramètres utilisés pendant l'entraînement pour une génération future
    with open(f'GanEntraine/{culture}gan_parameters.pkl', 'wb') as f:
        pickle.dump((latent_dim, num_cols, scaler), f)

def generate_data_from_gan(num_samples, culture):
    # Charger les paramètres
    with open('GanEntraine/'+culture+'gan_parameters.pkl', 'rb') as f:
        latent_dim, num_cols, scaler = pickle.load(f)

    # Charger les modèles entraînés
    # discriminator = load_model('discriminator_model.h5')
    generator = load_model('GanEntraine/'+culture+'generator_model.h5')

    # Charger le DataFrame pré-traité
    train_df = pd.read_csv('GanEntraine/'+culture+'train_df.csv')

    # Générer des points dans l'espace latent
    latent_points = sample_latent_points(latent_dim, num_samples)

    # Générer des échantillons avec le générateur
    generated_samples = generator.predict(latent_points)

    # Convertir les échantillons générés en un DataFrame
    generated_df = pd.DataFrame(generated_samples, columns=train_df.columns)

    # Appliquer la transformation inverse sur les colonnes numériques
    generated_df[num_cols] = scaler.inverse_transform(generated_df[num_cols])

    return generated_df