from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome: str
    preco: float

class ProdutoResponse(ProdutoCreate):
    id: int

    class Config:
        from_attributes = True