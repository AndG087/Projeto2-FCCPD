# Desafio 1 — Comunicação entre Containers

Este desafio mostra como dois containers podem se comunicar usando uma rede criada pelo Docker.  
Aqui temos um **servidor** na porta 8080 e um **cliente** que envia requisições para ele a cada poucos segundos.

---

## O que foi feito

- Criada a rede **`desafio1_net`**
- Servidor Flask rodando na porta **8080**
- Cliente que usa `curl` em loop para acessar o servidor
- `docker-compose` responsável por subir tudo na mesma rede

O cliente acessa o servidor usando o nome do serviço (`server`), sem precisar de IP.

---

## Estrutura do desafio

```
desafio1/
  docker-compose.yml
  server/
    Dockerfile
    app.py
  client/
    Dockerfile
    entrypoint.sh
```

---

## Como executar

Dentro da pasta do desafio:

```bash
docker-compose up
```

- O servidor ficará disponível em `http://localhost:8080/`
- O cliente começará a fazer requisições automaticamente

Ver os logs do cliente:

```bash
docker logs -f desafio1_client
```

Testar o servidor manualmente:

```bash
curl http://localhost:8080/
```

---

## Como parar

```bash
docker-compose down
```
