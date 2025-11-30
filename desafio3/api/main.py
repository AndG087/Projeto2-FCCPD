from fastapi import FastAPI
import psycopg2
import redis

app = FastAPI()

# Redis (cache)
cache = redis.Redis(host="cache", port=6379, db=0)

# Função para conectar ao PostgreSQL
def conectar_db():
    return psycopg2.connect(
        host="db",
        database="mensageria",
        user="appuser",
        password="app123"
    )

@app.get("/")
def raiz():
    # contador de acessos no Redis
    visitas = cache.incr("contador_visitas")

    # leitura no PostgreSQL
    conn = conectar_db()
    cur = conn.cursor()
    cur.execute("SELECT conteudo FROM mensagens;")
    mensagens = [m[0] for m in cur.fetchall()]
    cur.close()
    conn.close()

    return {
        "visitas": int(visitas),
        "mensagens_salvas_no_banco": mensagens
    }
