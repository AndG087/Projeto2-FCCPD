from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    hostname = socket.gethostname()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(
        message="Servidor HTTP respondendo com sucesso.",
        host=hostname,
        timestamp=now
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
