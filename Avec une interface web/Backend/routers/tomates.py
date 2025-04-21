from fastapi import APIRouter, Depends, HTTPException
import schemas
from methods import tomate  as methods
from fastapi.responses import FileResponse
from methods import graphe as gf



router = APIRouter(
     tags=['tomates'],
     prefix='/tomates',
)


@router.post("/genere",)
def Generated_tomates_data(request: schemas.Requetegenerees):
    
    methods.tomato_generator('data_genere/tomates_generated.csv', request.nb_lignes_generees,'tomato')
    return 'ok'


@router.post("/entraianement")
def Training_GAN(request: schemas.Requeteentrainement):
    return methods.tomato_train('data/tomates.csv', 100, request.nb_entrainement, 32, 100,'tomato')

@router.get("/donneInitiale")
def read_tomato():
    return FileResponse('data/tomates.csv', media_type='text/csv', filename='tomates.csv')


@router.get("/donneGenere")
def read_tomato_genere():
    return FileResponse('data_genere/tomates_generated.csv', media_type='text/csv', filename='tomates_generated.csv')

@router.post("/Graphique")
def Graphique(request: schemas.RequeteGraphe):
    df_base, df_generated = gf.charger_Fichier("csv", 'data/tomates.csv', 'data_genere/tomates_generated.csv')
    gf.plot_cumulative_frequency(request.param,'tomates', df_base, df_generated)
    gf.representer_selon_mois_boxplot(request.param, 'tomates', df_base, df_generated)
    gf.representer_selon_mois_histogramme(request.param, 'tomates', df_base, df_generated)