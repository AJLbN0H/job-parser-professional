FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root --with dev

COPY src/ ./src/
COPY tests/ ./tests/

RUN mkdir -p /app/data

ENV VACANCIES_FILE=/app/data/vacancies.json

CMD ["python", "-m", "src.main"]
