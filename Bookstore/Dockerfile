# --- Base Python ---
FROM python:3.13-slim as python-base

# --- Variáveis de ambiente ---
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.5.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# --- Instala dependências do sistema ---
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# --- Instala Poetry ---
RUN curl -sSL https://install.python-poetry.org | python3 -

# --- Diretório para setup das dependências ---
WORKDIR $PYSETUP_PATH

# --- Copia arquivos do Poetry para cache de dependências ---
COPY poetry.lock pyproject.toml ./

# --- Instala dependências (sem dev) ---
RUN poetry install --no-dev

# --- Diretório do projeto dentro do container ---
WORKDIR /app
COPY . /app/

# --- Porta padrão Django ---
EXPOSE 8000

# --- Comando para rodar o servidor Django ---
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
