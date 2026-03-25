# Usa uma imagem leve do Python
FROM python:3.11-slim

# Define onde as coisas vão acontecer dentro do container
WORKDIR /app

# Instala dependências do sistema necessárias para o psycopg2 (banco de dados)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do seu código para dentro do container
COPY . .

# Comando para iniciar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]