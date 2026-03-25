````markdown
# API de Produtos com FastAPI, PostgreSQL e Redis (Dockerized)

Este projeto é uma API simples para gerenciamento de produtos, desenvolvida para demonstrar o uso de **Docker Compose** na orquestração de múltiplos serviços (Backend, Banco de Dados e Cache).

## 🛠 Tecnologias Utilizadas

* **Python 3.11** com **FastAPI** (Framework Web)
* **PostgreSQL 16** (Banco de Dados Relacional)
* **Redis 7** (Cache em memória)
* **SQLAlchemy** (ORM para persistência de dados)
* **Pydantic** (Validação de schemas e dados)
* **Docker & Docker Compose** (Containerização e Orquestração)

## 🏗 Arquitetura do Projeto

A aplicação utiliza uma arquitetura moderna dividida em três serviços principais:
1.  **API**: Backend que gerencia a lógica de negócios e as rotas.
2.  **Postgres**: Armazenamento persistente de produtos.
3.  **Redis**: Camada de cache para otimizar a performance da rota de listagem (`GET /produtos`).



## ⚡ Como Rodar o Projeto

### 1. Pré-requisitos
* Possuir o **Docker** e o **Docker Compose** instalados na máquina.

### 2. Configuração das Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz do projeto e preencha com as seguintes variáveis (ou use o exemplo abaixo):

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=sua_senha_secreta
POSTGRES_DB=padaria_db
DATABASE_URL=postgresql://admin:sua_senha_secreta@postgres:5432/padaria_db
REDIS_URL=redis://redis:6379/0
````

### 3\. Subir o ambiente

No terminal, dentro da pasta do projeto, execute:

```bash
docker-compose up --build
```

O Docker irá baixar as imagens, buildar a API e configurar as redes automaticamente. A API estará disponível em: `http://localhost:8000`.

## 🚀 Endpoints e Documentação

O FastAPI gera automaticamente a documentação Interativa (Swagger). Acesse:

  * **Swagger UI**: [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)

### Rotas Disponíveis:

  * `GET /health`: Verifica o status da API.
  * `POST /produtos`: Cria um novo produto (id, nome, preco).
  * `GET /produtos`: Lista todos os produtos (com cache de 60s no Redis).

## ❄️ Implementação de Cache

Para garantir alta performance, a listagem de produtos utiliza **Redis**.

  * No primeiro acesso, os dados são buscados no **PostgreSQL** (**Cache Miss**).
  * Nos acessos seguintes (dentro de 60s), os dados são entregues instantaneamente pelo **Redis** (**Cache Hit**).
  * Ao cadastrar um novo produto, o cache é automaticamente invalidado para garantir a consistência dos dados.

-----

Projeto desenvolvido para fins acadêmicos - Atividade de DevOps.

```