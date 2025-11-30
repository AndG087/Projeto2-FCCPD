from fastapi import FastAPI
import requests

app = FastAPI()

URL_MICROSSERVICO_USUARIOS = "http://service_usuarios:8000/usuarios"


@app.get("/relatorio-usuarios")
def relatorio_usuarios():
    """
    Consome o microsserviço de usuários e monta frases com as informações.
    """
    try:
        resposta = requests.get(URL_MICROSSERVICO_USUARIOS)
        resposta.raise_for_status()
        dados = resposta.json()

        usuarios = dados.get("usuarios", [])

        frases = []
        for u in usuarios:
            nome = u.get("nome")
            ano = u.get("ano_entrada")
            ativo = u.get("ativo")

            situacao = "ativo" if ativo else "inativo"
            frases.append(f"{nome} está {situacao} e faz parte do sistema desde {ano}.")

        return {"relatorio": frases}

    except requests.RequestException as e:
        return {"erro": f"Falha ao consultar o serviço de usuários: {str(e)}"}
