from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def head_root():
    return {"health": "API rodando"}

