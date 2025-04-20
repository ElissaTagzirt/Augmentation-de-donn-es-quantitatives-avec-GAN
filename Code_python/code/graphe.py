import pandas as pd
import matplotlib  # Ajouté
matplotlib.use('Agg')  # Ajouté pour définir le backend avant d'importer pyplot
import matplotlib.pyplot as plt
def charger_Fichier(type, chemin_vers_fichier_base, chemin_vers_fichier_generated):
    # Lecture fichier de base
    if type == "csv":
        df_base = pd.read_csv(chemin_vers_fichier_base)
    else: 
        df_base = pd.read_excel(chemin_vers_fichier_base)
    # Lecture fichier résultat de data augmentation
    df_generated = pd.read_csv(chemin_vers_fichier_generated)
    return df_base, df_generated

def representer_selon_mois_histogramme(param, culture, df_base, df_generated):
    # Calculer la moyenne du Water Requirement par mois
    mean_water_req_base = df_base.groupby('month')[param].mean()
    mean_water_req_generated = df_generated.groupby('month')[param].mean()

    # Créer le graphique en barres
    plt.figure(figsize=(10, 6))
    plt.bar(mean_water_req_base.index, mean_water_req_base.values, color='green', label='Données initiales', alpha=0.5)
    plt.bar(mean_water_req_generated.index, mean_water_req_generated.values, color='yellow', label='Données générées', alpha=0.5)
    plt.xlabel('Mois')
    plt.ylabel('Moyenne de '+param)
    plt.title(culture+' : Moyenne de '+param+' selon Month')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Enregistrer le graphique au format PNG
    plt.savefig('./Qualité/'+culture+'histo_month_'+param+'.png')

def representer_boxplot(param, culture, df_base, df_generated):
    # Créer le graphique en boîte à moustaches
    plt.figure(figsize=(10, 6))
    bp = plt.boxplot([df_base[param], df_generated[param]], labels=['Données initiales', 'Données générées'], patch_artist=True, medianprops=dict(color='red'))

    # Couleur des boîtes
    colors = ['green', 'yellow']
    for box, color in zip(bp['boxes'], colors):
        box.set(color=color, linewidth=2)
        box.set(facecolor=color, alpha=0.5)

    # Afficher la médiane, le minimum, le maximum, Q1 et Q3
    for i, data in enumerate([df_base[param], df_generated[param]]):
        median = data.median()
        minimum = data.min()
        maximum = data.max()
        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)
        plt.text(i + 1, median, f'Médiane: {median:.2f}', horizontalalignment='right', verticalalignment='bottom', fontweight='bold')
        plt.text(i + 1, minimum, f'Min: {minimum:.2f}', horizontalalignment='right', verticalalignment='bottom')
        plt.text(i + 1, maximum, f'Max: {maximum:.2f}', horizontalalignment='right', verticalalignment='bottom')
        plt.text(i + 1, q1, f'Q1: {q1:.2f}', horizontalalignment='right', verticalalignment='top')
        plt.text(i + 1, q3, f'Q3: {q3:.2f}', horizontalalignment='right', verticalalignment='bottom')

    plt.ylabel(param)
    plt.title('Boxplot de '+culture+' selon la variable '+param)
    plt.grid(True)
    plt.tight_layout()
    
    # Enregistrer le graphique au format PNG
    plt.savefig('./Qualité/'+culture+'boxplot_'+ param +'.png')

def plot_cumulative_frequency(param, culture, df_base, df_generated):
    # Calculer la fréquence cumulative
    cumulative_freq_base = df_base[param].value_counts().sort_index().cumsum()
    cumulative_freq_generated = df_generated[param].value_counts().sort_index().cumsum()

    # Tracer le graphique de la fréquence cumulative
    plt.figure(figsize=(10, 6))
    plt.plot(cumulative_freq_base.index, cumulative_freq_base.values, label='Base Data', marker='o', color='green')
    plt.plot(cumulative_freq_generated.index, cumulative_freq_generated.values, label='Generated Data', marker='o', color='yellow')
    plt.xlabel(param)
    plt.ylabel('Fréquences cumulées')
    plt.title('Fréquences cumulées de la variable '+param+' pour '+culture)
    plt.legend()
    plt.grid(True)

    # Enregistrer le graphique au format PNG
    plt.savefig('./Qualité/'+culture+'cumulative_'+ param +'.png')
    #plt.show()
