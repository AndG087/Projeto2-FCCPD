from fastapi import FastAPI

app = FastAPI()

USERS = [
    {"id": 1, "nome": "Clara", "email": "clara@example.com"},
    {"id": 2, "nome": "Renato", "email": "renato@example.com"},
    {"id": 3, "nome": "Paulo", "email": "paulo@example.com"},
]


@app.get("/users")
def listar_usuarios():
    return {"users": USERS}
