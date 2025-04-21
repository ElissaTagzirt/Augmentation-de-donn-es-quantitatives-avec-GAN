from fastapi import APIRouter
import schemas
from methods import ble  as methods
from fastapi.responses import FileResponse
from methods import graphe as gf



router = APIRouter(
     tags=['ble'],
     prefix='/ble',
)


@router.post("/genere",)
def Generated_ble(request: schemas.Requetegenerees):
    return methods.ble_generator('data_genere/ble_generated.csv', request.nb_lignes_generees,'ble')

@router.post("/entraianement")
def Training_GAN(request: schemas.Requeteentrainement):
    return methods.ble_train('data/ble.csv', 100, request.nb_entrainement, 32, 100 ,'ble')

@router.get("/donneInitiale")
def read_ble():
    return FileResponse('data/ble.csv', media_type='text/csv', filename='ble.csv')


@router.get("/donneGenere")
def read_ble_genere():
    return FileResponse('data_genere/ble_generated.csv', media_type='text/csv', filename='ble_generated.csv')

@router.post("/Graphique")
def Graphique(request: schemas.RequeteGraphe):
    df_base, df_generated = gf.charger_Fichier("csv", 'data/ble.csv', 'data_genere/ble_generated.csv')
    gf.plot_cumulative_frequency(request.param,'ble', df_base, df_generated)
    gf.representer_selon_mois_boxplot(request.param,'ble', df_base, df_generated)
    gf.representer_selon_mois_histogramme(request.param,'ble', df_base, df_generated)