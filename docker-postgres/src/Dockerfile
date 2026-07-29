FROM python:3.13-slim

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
COPY data/ ./data/
COPY queries/ ./queries/

CMD ["tail", "-f", "/dev/null"]
## comando para mantener despierto al contenedor src_container_

## Si quiero correrlo manualmente dentro del contenedor, puedo hacerlo con el siguiente comando:
## docker compose run --rm --entrypoint bash src