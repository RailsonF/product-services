from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .models import Produto
from .schemas import ProdutoCreate, ProdutoResponse

# Cria as tabelas assim que a API inicia
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def head_root():
    return {"health": "API rodando"}

@app.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()

@app.post("/produtos", response_model=ProdutoResponse)
def criar_produto(produto_in: ProdutoCreate, db: Session = Depends(get_db)):
    
    # Transforma o schema do Pydantic em um modelo do SQLAlchemy
    novo_produto = Produto(nome=produto_in.nome, preco=produto_in.preco)
    
    # Adiciona e salva no banco
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto) # Pega o ID gerado pelo banco
    
    return novo_produto
