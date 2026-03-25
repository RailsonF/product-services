import redis
import json
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from .models import Produto
from .schemas import ProdutoCreate, ProdutoResponse

# Configuração do Redis (Lendo a variável de ambiente injetada pelo Docker)
import os
redis_client = redis.from_url(os.getenv("REDIS_URL", "redis://redis:6379/0"), decode_responses=True)

# Cria as tabelas assim que a API inicia
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def head_root():
    return {"health": "API rodando"}

@app.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    cache_key = "lista_produtos"

    # Tenta buscar no Cache (Redis)
    produtos_cache = redis_client.get(cache_key)
    if produtos_cache:
        print("--- CACHE HIT: Retornando do Redis ---")
        return json.loads(produtos_cache)
    
    # Se não estiver no cache, buscar no Banco (Postgres)
    print("--- CACHE MISS: Indo ao Postgres ---")
    produtos = db.query(Produto).all()
    
    # Transformar a lista de objetos do banco em uma lista de dicionários para o JSON
    produtos_lista = [
        {"id": p.id, "nome": p.nome, "preco": p.preco} for p in produtos
    ]
    
    # Salvar no Redis por 60 segundos (para não ficar obsoleto para sempre)
    redis_client.setex(cache_key, 60, json.dumps(produtos_lista))
    
    return produtos_lista

@app.post("/produtos", response_model=ProdutoResponse)
def criar_produto(produto_in: ProdutoCreate, db: Session = Depends(get_db)):
    
    # Transforma o schema do Pydantic em um modelo do SQLAlchemy
    novo_produto = Produto(nome=produto_in.nome, preco=produto_in.preco)
    
    # Adiciona e salva no banco
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto) # Pega o ID gerado pelo banco

    # Limpar o cache para que o próximo GET busque a lista atualizada
    redis_client.delete("lista_produtos")
    
    return novo_produto
