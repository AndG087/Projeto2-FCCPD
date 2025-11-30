import psycopg2
import time

time.sleep(5)

while True:
    try:
        conn = psycopg2.connect(
            host="database",
            user="admin",
            password="admin123",
            dbname="loja"
        )
        cur = conn.cursor()
        cur.execute("SELECT id, nome, preco FROM produtos;")
        rows = cur.fetchall()

        print("Produtos cadastrados:")
        for r in rows:
            print(f"- {r[1]} (R$ {r[2]:.2f})")

        cur.close()
        conn.close()

    except Exception as e:
        print("Erro ao conectar:", e)

    time.sleep(5)
