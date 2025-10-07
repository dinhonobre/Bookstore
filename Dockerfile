# --- Base Python ---
FROM python:3.13-slim

# --- Variáveis de ambiente ---
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# --- Instala dependências do sistema ---
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# --- Diretório do projeto ---
WORKDIR /app

# --- Copia todo o código da aplicação ---
COPY . /app/

# --- Instala Poetry e as dependências diretamente no Python global ---
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.5.1 && \
    /root/.local/bin/poetry config virtualenvs.create false && \
    /root/.local/bin/poetry install --only main

# --- Porta padrão Django ---
EXPOSE 8000

# --- Comando para rodar o servidor Django ---
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
