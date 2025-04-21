from fastapi import APIRouter, Depends, HTTPException
import schemas
from methods import website  as methods
from fastapi.responses import FileResponse
from methods import conversionfichier as cv
from methods import graphe as gf




router = APIRouter(
     tags=['websitedata'],
     prefix='/websitedata',
)


@router.post("/genere")
def Generated_websitedata_data(request: schemas.Requetegenerees):
    return methods.generate_data_from_gan('data_genere/website_generated.csv',request.nb_lignes_generees,'website')



@router.post("/entraianement")
def Training_GAN(request: schemas.Requeteentrainement):
    return methods.train_gan('data/Website_data.xlsx', 100, request.nb_entrainement, 32, 100,'website')

    
    
@router.get("/donneBrute")
def read_websitedata_data():
    return FileResponse('data/Website_data.csv', media_type='text/csv', filename='Website_data.csv')

@router.get("/donneGenere")
def read_websitedata_data_genere():
    return FileResponse('data_genere/website_generated.csv', media_type='text/csv', filename='website_generated.csv')

@router.get("/comparative")
def read_websitedata_data_genere():
    return FileResponse('data_genere/website_initiale_comparative.csv', media_type='text/csv', filename='website_initiale_comparative.csv')

@router.post("/Graphique")
def Graphique(request: schemas.RequeteGraphe):
    df_base, df_generated = gf.charger_Fichier("csv", 'data_genere/website_initiale_comparative.csv', 'data_genere/website_generated_comprative.csv')
    gf.plot_cumulative_frequency(request.param,'Website', df_base, df_generated)
    gf.representer_selon_mois_boxplot(request.param,'Website', df_base, df_generated)
    gf.representer_selon_mois_histogramme(request.param,'Website', df_base, df_generated)
    return "ok"