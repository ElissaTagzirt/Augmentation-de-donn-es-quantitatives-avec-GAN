from fastapi import APIRouter, Depends, HTTPException
import schemas
from methods import mais  as methods
from fastapi.responses import FileResponse
from methods import graphe as gf



router = APIRouter(
     tags=['mais'],
     prefix='/mais',
)


@router.post("/genere",)
def Generated_mais_data(request: schemas.Requetegenerees):
    methods.mais_generator('data_genere/maïs_generated.csv', request.nb_lignes_generees,'mais')
    return 'ok'

@router.post("/entraianement")
def Training_GAN(request: schemas.Requeteentrainement):
    return methods.mais_train('data/maïs.xlsx', 100, request.nb_entrainement, 32, 100,'mais')



@router.get("/donneInitiale")
def read_websitedata_data():
    return FileResponse('data/maïs.csv', media_type='text/csv', filename='maïs.csv')

@router.get("/donneGenere")
def read_mais_genere():
    return FileResponse('data_genere/maïs_generated.csv', media_type='text/csv', filename='maïs_generated.csv')


@router.post("/Graphique")
def Graphique(request: schemas.RequeteGraphe):
    df_base, df_generated = gf.charger_Fichier("csv", 'data/maïs.csv', 'data_genere/maïs_generated.csv')
    gf.plot_cumulative_frequency(request.param,'maïs', df_base, df_generated)
    gf.representer_selon_mois_boxplot(request.param, 'maïs', df_base, df_generated)
    gf.representer_selon_mois_histogramme(request.param, 'maïs', df_base, df_generated)