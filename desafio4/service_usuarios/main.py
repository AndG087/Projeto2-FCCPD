from fastapi import FastAPI
from datetime import date

app = FastAPI()


usuarios = [
    {"id": 1, "nome": "Ana", "ano_entrada": 2020, "ativo": True},
    {"id": 2, "nome": "Bruno", "ano_entrada": 2022, "ativo": True},
    {"id": 3, "nome": "Carla", "ano_entrada": 2019, "ativo": False},
]


@app.get("/usuarios")
def listar_usuarios():
    """Retorna a lista de usuários em formato JSON."""
    return {"usuarios": usuarios}


@app.get("/status")
def status():
    """Endpoint simples só para teste de saúde do serviço."""
    return {"status": "ok", "total_usuarios": len(usuarios)}
