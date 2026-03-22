from fastapi import FastAPI

from database import start_db
from routers.species import router as species_router

app = FastAPI()


@app.on_event("startup")
def on_startup():
    start_db()


@app.get("/")
def root():
    return {"message": "Bird API is running"}


app.include_router(species_router)