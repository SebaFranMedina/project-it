FROM python:3.13-slim
 
WORKDIR /app
 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
COPY extract-data.py .
 
CMD ["python", "extract-data.py"]
 

## Si quiero correrlo manualmente dentro del contenedor, puedo hacerlo con el siguiente comando:
## docker compose run --rm --entrypoint bash src