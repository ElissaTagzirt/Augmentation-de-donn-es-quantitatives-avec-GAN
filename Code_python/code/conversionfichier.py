import pandas as pd

def xlsx_to_csv(xlsx_path, csv_path):
    # Lire le fichier .xlsx
    df = pd.read_excel(xlsx_path, engine='openpyxl')
    # Sauvegarder en tant que fichier .csv
    df.to_csv(csv_path, index=False)
    return 'cest bon'
