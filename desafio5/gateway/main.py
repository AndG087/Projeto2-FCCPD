from fastapi import FastAPI
import requests

app = FastAPI()

USERS_SERVICE_URL = "http://usuarios:8001/users"
ORDERS_SERVICE_URL = "http://pedidos:8002/orders"


@app.get("/users")
def gateway_users():
    try:
        resp = requests.get(USERS_SERVICE_URL, timeout=3)
        resp.raise_for_status()
        dados = resp.json()
        return {"source": "usuarios-service", "data": dados}
    except Exception as e:
        return {"error": "Falha ao consultar serviço de usuários", "details": str(e)}


@app.get("/orders")
def gateway_orders():
    try:
        resp = requests.get(ORDERS_SERVICE_URL, timeout=3)
        resp.raise_for_status()
        dados = resp.json()
        return {"source": "pedidos-service", "data": dados}
    except Exception as e:
        return {"error": "Falha ao consultar serviço de pedidos", "details": str(e)}
