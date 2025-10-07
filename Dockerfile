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
    PATH="/opt/poetry/bin:$VENV_PATH/bin:$PATH"

# --- Instala dependências do sistema ---
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential \
        libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# --- Instala Poetry ---
RUN curl -sSL https://install.python-poetry.org | python3 -

# --- Garante que o Poetry está no PATH ---
ENV PATH="/opt/pysetup/.venv/bin:$PATH"


# --- Diretório para setup das dependências ---
WORKDIR /opt/pysetup
COPY poetry.lock pyproject.toml README.md ./
COPY Bookstore ./Bookstore
RUN /opt/poetry/bin/poetry install --only main


# --- Diretório do projeto dentro do container ---
WORKDIR /app
COPY . /app/

# --- Porta padrão Django ---
EXPOSE 8000

# --- Comando para rodar o servidor Django ---
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


