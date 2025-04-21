from pydantic import BaseModel


class Requeteentrainement(BaseModel):
    nb_entrainement : int

class Requetegenerees(BaseModel):
    nb_lignes_generees : int
    
class RequeteGraphe(BaseModel):
    param : str
 