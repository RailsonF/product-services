from fastapi import FastAPI
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .models import Produto

# Cria as tabelas assim que a API inicia
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def head_root():
    return {"health": "API rodando"}

