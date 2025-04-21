from fastapi import APIRouter, Depends, HTTPException
import schemas
from methods import riz as methods
from fastapi.responses import FileResponse
from methods import graphe as gf



router = APIRouter(
     tags=['riz'],
     prefix='/riz',
)


@router.post("/genere",)
def Generated_riz_data(request: schemas.Requetegenerees):
    methods.riz_generator('data_genere/riz_generated.csv', request.nb_lignes_generees,'riz')
    return 'ok'


@router.post("/entraianement")
def Training_GAN(request: schemas.Requeteentrainement):
    return methods.riz_train('data/riz.csv', 100, request.nb_entrainement, 32, 100,'riz')

@router.get("/donneInitiale")
def read_riz():
    return FileResponse('data/riz.csv', media_type='text/csv', filename='riz.csv')



@router.get("/donneGenere")
def read_riz_genere():
    return FileResponse('data_genere/riz_generated.csv', media_type='text/csv', filename='riz_generated.csv')


@router.post("/Graphique")
def Graphique(request: schemas.RequeteGraphe):
    df_base, df_generated = gf.charger_Fichier("csv", 'data/riz.csv', 'data_genere/riz_generated.csv')
    gf.plot_cumulative_frequency(request.param,'riz', df_base, df_generated)
    gf.representer_selon_mois_boxplot(request.param,'riz', df_base, df_generated)
    gf.representer_selon_mois_histogramme(request.param, 'riz', df_base, df_generated)