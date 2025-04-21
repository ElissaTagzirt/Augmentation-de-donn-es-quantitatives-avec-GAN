from fastapi import APIRouter
import schemas
from methods import plants  as methods
from fastapi.responses import FileResponse
from methods import graphe as gf



router = APIRouter(
     tags=['dataPalntes'],
     prefix='/dataPalntes',
)


@router.post("/genere",)
def Generated_data_plants_data(request: schemas.Requetegenerees):
     methods.plants_generator('data_genere/data_plants_generated.csv', request.nb_lignes_generees,'plants')
     return 'ok'

@router.post("/entraianement")
def Training_GAN(request: schemas.Requeteentrainement):
    return methods.plants_train('data/data_plants.csv', 100, request.nb_entrainement, 32, 100,'plants')

@router.get("/donneInitiale")
def read_data_plants():
    return FileResponse('data/data_plants.csv', media_type='text/csv', filename='data_plants.csv')


@router.get("/donneGenere")
def read_data_plants_genere():
    return FileResponse('data_genere/data_plants_generated.csv', media_type='text/csv', filename='data_plants_generated.csv')

@router.post("/Graphique")
def Graphique(request: schemas.RequeteGraphe):
    df_base, df_generated = gf.charger_Fichier("csv", 'data/data_plants.csv', 'data_genere/data_plants_generated.csv')
    gf.plot_cumulative_frequency(request.param,'data_plants', df_base, df_generated)
    gf.representer_selon_mois_boxplot(request.param, 'data_plants', df_base, df_generated)
    gf.representer_selon_mois_histogramme(request.param, 'data_plants', df_base, df_generated)