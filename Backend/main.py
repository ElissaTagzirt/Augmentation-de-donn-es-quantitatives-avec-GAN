from fastapi import FastAPI
from routers import ble , arachides_riz , data_plans , mais , potato , riz , tomates , websitedata
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello"}


app.include_router(ble.router)
app.include_router(arachides_riz.router)
app.include_router( data_plans.router)
app.include_router(mais.router)
app.include_router(potato.router)
app.include_router(riz.router)
app.include_router(tomates.router)
app.include_router(websitedata.router)

