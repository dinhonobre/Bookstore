# --- Base Python ---
FROM python:3.13-slim

# --- Variáveis de ambiente ---
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.5.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    PATH="$POETRY_HOME/bin:$PATH"

# --- Instala dependências do sistema ---
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# --- Instala Poetry ---
RUN curl -sSL https://install.python-poetry.org | python3 -

# --- Diretório do projeto ---
WORKDIR /app

# --- Copia arquivos de dependências primeiro para cache do Docker ---
COPY pyproject.toml poetry.lock* /app/

# --- Instala dependências sem criar virtualenv isolada ---
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# --- Copia o restante do projeto ---
COPY . /app/

# --- Porta padrão Django ---
EXPOSE 8000

# --- Comando para rodar o servidor Django ---
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
