# --- Base Python ---
FROM python:3.13-slim

# --- Variáveis de ambiente ---
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.3 \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/root/.local" \
    PATH="/root/.local/bin:$PATH"

# --- Instala dependências do sistema ---
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl build-essential libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# --- Instala Poetry ---
RUN curl -sSL https://install.python-poetry.org | python3 -

# --- Define diretório de trabalho ---
WORKDIR /app

# --- Copia arquivos de dependências ---
COPY pyproject.toml poetry.lock* /app/

# --- Instala dependências (sem virtualenv isolada e sem root package) ---
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi --no-root

# --- Copia o restante do projeto ---
COPY . /app/

# --- Expõe a porta padrão do Django ---
EXPOSE 8000

# --- Comando para rodar o servidor ---
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
