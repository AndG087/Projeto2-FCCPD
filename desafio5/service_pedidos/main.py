from fastapi import FastAPI

app = FastAPI()

ORDERS = [
    {"id": 1, "user_id": 1, "item": "Livro de Redes", "valor": 120.50},
    {"id": 2, "user_id": 2, "item": "Teclado Mecânico", "valor": 350.00},
    {"id": 3, "user_id": 1, "item": "Headset", "valor": 220.00},
]


@app.get("/orders")
def listar_pedidos():
    return {"orders": ORDERS}
