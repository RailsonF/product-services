````markdown
# API de Produtos com FastAPI, PostgreSQL e Redis (Dockerized)

Este projeto é uma API simples para gerenciamento de produtos, desenvolvida para demonstrar o uso de **Docker Compose** na orquestração de múltiplos serviços (Backend, Banco de Dados e Cache).

## 🛠 Tecnologias Utilizadas

- **Python 3.11** com **FastAPI** (framework web)
- **PostgreSQL 16** (banco de dados relacional)
- **Redis 7** (cache em memória)
- **SQLAlchemy** (ORM para persistência de dados)
- **Pydantic** (validação de schemas e dados)
- **Docker & Docker Compose** (containerização e orquestração)

## 🏗 Arquitetura do Projeto

A aplicação utiliza uma arquitetura moderna dividida em três serviços principais:

1. **API**: Backend responsável pela lógica de negócios e rotas.
2. **Postgres**: Armazenamento persistente de produtos.
3. **Redis**: Camada de cache para otimizar a performance da rota de listagem (`GET /produtos`).

## ⚡ Como Rodar o Projeto

### 1. Pré-requisitos

- Ter o **Docker** e o **Docker Compose** instalados na máquina.

### 2. Configuração das Variáveis de Ambiente

Crie um arquivo chamado `.env` na raiz do projeto e preencha com as seguintes variáveis:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=sua_senha_secreta
POSTGRES_DB=padaria_db
DATABASE_URL=postgresql://admin:sua_senha_secreta@postgres:5432/padaria_db
REDIS_URL=redis://redis:6379/0
````

### 3. Subir o ambiente

No terminal, dentro da pasta do projeto, execute:

```bash
docker-compose up --build
```

O Docker irá baixar as imagens, buildar a API e configurar as redes automaticamente.

A API estará disponível em:
👉 [http://localhost:8000](http://localhost:8000)

## 🚀 Endpoints e Documentação

O FastAPI gera automaticamente a documentação interativa (Swagger). Acesse:

* **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)

### Rotas Disponíveis

* `GET /health`: Verifica o status da API.
* `POST /produtos`: Cria um novo produto (`id`, `nome`, `preco`).
* `GET /produtos`: Lista todos os produtos (com cache de 60s no Redis).

## ❄️ Implementação de Cache

Para garantir alta performance, a listagem de produtos utiliza **Redis**:

* No primeiro acesso, os dados são buscados no **PostgreSQL** (**cache miss**).
* Nos acessos seguintes (dentro de 60s), os dados são entregues instantaneamente pelo **Redis** (**cache hit**).
* Ao cadastrar um novo produto, o cache é automaticamente invalidado para garantir a consistência dos dados.

---

Projeto desenvolvido para fins acadêmicos — atividade de DevOps.

```
```
