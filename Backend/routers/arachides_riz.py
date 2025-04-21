from fastapi import APIRouter
import schemas
from methods import arachides_riz  as methods
from fastapi.responses import FileResponse
from methods import graphe as gf



router = APIRouter(
     tags=['arachides_riz'],
     prefix='/arachides_riz',
)

schemas.Requeteentrainement
@router.post("/genere",)
def Generated_arachides_riz(request: schemas.Requetegenerees):
    return methods.arachides_riz_generator('data_genere/arachides_riz_generated.csv',request.nb_lignes_generees,'arachide')

@router.post("/entrainement")
def Training_GAN(request: schemas.Requeteentrainement):
    return methods.arachides_riz_train('data/arachides_riz.xlsx', 100, request.nb_entrainement, 32, 100, 'arachide')



@router.get("/donneInitiale")
def read_websitedata_data():
    return FileResponse('data/arachides_riz.csv', media_type='text/csv', filename='arachides_riz.csv')

@router.get("/donneGenere")
def read_arachides_riz_genere():
    return FileResponse('data_genere/arachides_riz_generated.csv', media_type='text/csv', filename='arachides_riz_generated.csv')

@router.post("/Graphique")
def Graphique(request: schemas.RequeteGraphe):
    df_base, df_generated = gf.charger_Fichier("csv", 'data/arachides_riz.csv', 'data_genere/arachides_riz_generated.csv')
    gf.plot_cumulative_frequency(request.param,'arachides_riz', df_base, df_generated)
    gf.representer_selon_mois_boxplot(request.param, 'arachides_riz', df_base, df_generated)
    gf.representer_selon_mois_histogramme(request.param, 'arachides_riz', df_base, df_generated)
