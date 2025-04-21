from fastapi import APIRouter, Depends, HTTPException
import schemas
from methods import potato  as methods
from methods import graphe as gf
from fastapi.responses import FileResponse




router = APIRouter(
     tags=['potato'],
     prefix='/potato',
)


@router.post("/genere",)
def Generated_potato_data(request: schemas.Requetegenerees):
     methods.potato_generator('data_genere/potato_generated.csv',request.nb_lignes_generees,'potato')
     return 'ok'

@router.post("/entraianement")
def Training_GAN(request: schemas.Requeteentrainement):
    return methods.potato_train('data/potato.csv', 100,request.nb_entrainement, 32, 100,'potato')

@router.get("/donneInitiale")
def read_potatoes():
    return FileResponse('data/potato.csv', media_type='text/csv', filename='potato.csv')

@router.get("/donneGenere")
def read_potatoes_genere():
    return FileResponse('data_genere/potato_generated.csv', media_type='text/csv', filename='potato_generated.csv')

@router.post("/Graphique")
def Graphique(request: schemas.RequeteGraphe):
    df_base, df_generated = gf.charger_Fichier("csv", 'data/potato.csv', 'data_genere/potato_generated.csv')
    gf.plot_cumulative_frequency(request.param,'potato', df_base, df_generated)
    gf.representer_selon_mois_boxplot(request.param, 'potato', df_base, df_generated)
    gf.representer_selon_mois_histogramme(request.param, 'potato', df_base, df_generated)
    return 'ok'
  
