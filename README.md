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

# Desafio 4 — Microsserviços independentes

Neste desafio foram criados dois microsserviços separados que se comunicam via HTTP:

- um serviço de **usuários** (service_usuarios),
- e um serviço de **relatórios** (service_relatorios) que consome o primeiro.

A ideia é mostrar a comunicação entre serviços independentes usando requisições HTTP dentro de uma mesma rede Docker.

---

## Visão geral

- O **service_usuarios** expõe um endpoint `/usuarios` que retorna uma lista em JSON com informações de usuários.
- O **service_relatorios** chama esse endpoint, processa os dados recebidos e devolve frases prontas em `/relatorio-usuarios`.

Cada serviço tem seu próprio Dockerfile e suas próprias dependências.

---

## Estrutura do desafio

```text
desafio4/
  docker-compose.yml
  service_usuarios/
    Dockerfile
    main.py
    requirements.txt
  service_relatorios/
    Dockerfile
    main.py
    requirements.txt
```

---

## Como executar

Na pasta do desafio:

```bash
cd desafio4
docker-compose up
```

Isso vai:

- subir o **service_usuarios** (FastAPI na porta interna 8000, exposta como 7000 no host),
- subir o **service_relatorios** (FastAPI na porta interna 8001, exposta como 7001 no host),
- configurar a rede interna `rede_interna` para os dois serviços se enxergarem.

---

## Testando os serviços

### 1. Microsserviço de usuários

No navegador ou via `curl`:

```bash
curl http://localhost:7000/usuarios
```

Retorna um JSON com a lista de usuários.

### 2. Microsserviço de relatórios

```bash
curl http://localhost:7001/relatorio-usuarios
```

Retorna um JSON com frases montadas a partir dos dados do serviço de usuários, por exemplo:

```json
{
  "relatorio": [
    "Ana está ativa e faz parte do sistema desde 2020.",
    "Bruno está ativo e faz parte do sistema desde 2022.",
    "Carla está inativa e faz parte do sistema desde 2019."
  ]
}
```

---

## Como parar

```bash
docker-compose down
```
