FROM python:3.11.2-slim-buster

RUN apt-get update \
&& apt-get install build-essential -y \
&& pip install poetry

COPY ./pyproject.toml /app/
WORKDIR /app/
RUN poetry install --no-dev

# Install app
COPY ./api /app/api
RUN poetry install --no-dev
ENTRYPOINT poetry run uvicorn api.main:app --reload --host 0.0.0.0 --port 8080