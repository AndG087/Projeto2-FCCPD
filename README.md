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


# Desafio 2 — Persistência com Volumes no Docker

O objetivo deste desafio é mostrar que os dados do banco continuam existindo mesmo depois que o container é removido.  
Para isso, montei um pequeno banco PostgreSQL com volume e um leitor em Python que consulta os dados.

---

## O que foi feito

- Usei um container PostgreSQL que roda um script SQL automaticamente.
- Os dados são salvos em um volume chamado **dados_pg**.
- Criei um segundo container que se conecta ao banco e imprime os produtos cadastrados.
- Removi e subi o container novamente para confirmar que os dados permaneceram.

---

## Estrutura do desafio

```
desafio2/
  docker-compose.yml
  init.sql
  reader/
    Dockerfile
    reader.py
```

---

## Como executar

Entre na pasta do desafio:

```bash
cd desafio2
```

Suba os containers:

```bash
docker-compose up
```

O leitor vai tentar acessar o banco e mostrar a lista de produtos cadastrados.

---

## Testando a persistência

Derrube tudo:

```bash
docker-compose down
```

Suba novamente:

```bash
docker-compose up -d
```

Cheque os dados:

```bash
docker exec -it desafio2_pg psql -U admin -d loja -c "SELECT * FROM produtos;"
```

Os produtos continuam lá graças ao volume **dados_pg**.

---

## Como parar

```bash
docker-compose down
```
# Desafio 3 — Orquestração de 3 serviços com Docker Compose

Neste desafio foi criada uma aplicação composta por **três serviços** trabalhando juntos:

- uma API em **FastAPI** (web),
- um banco **PostgreSQL** (db),
- e um serviço de **Redis** (cache).

O objetivo é usar o Docker Compose para subir todos esses serviços, configurar a comunicação entre eles e demonstrar que a API acessa tanto o banco quanto o cache.

---

## O que a aplicação faz

Sempre que a rota principal (`/`) é acessada:

1. Um contador no Redis é incrementado.
2. A API busca no PostgreSQL todas as mensagens da tabela `mensagens`.
3. A resposta junta as duas informações em um JSON.

Exemplo de resposta:

```json
{
  "visitas": 4,
  "mensagens_salvas_no_banco": [
    "Bem-vindo ao sistema!",
    "Mensagem registrada com sucesso.",
    "Dados carregados do PostgreSQL."
  ]
}
```

---

## Estrutura do desafio

```
desafio3/
  docker-compose.yml
  api/
    Dockerfile
    main.py
    requirements.txt
  db/
    init.sql
```

---

## Como executar

Dentro da pasta do desafio:

```bash
docker-compose up
```

Quando tudo estiver rodando, acesse:

```
http://localhost:8081/
```

Cada refresh da página aumenta o contador no Redis.

---

## Como verificar os dados do banco

```bash
docker exec -it desafio3_db psql -U appuser -d mensageria -c "SELECT * FROM mensagens;"
```

---

## Como parar tudo

```bash
docker-compose down
```

Isso derruba os containers, mas o volume `pgdata3` mantém os dados do banco.

