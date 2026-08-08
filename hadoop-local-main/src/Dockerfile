FROM python:3.13-slim

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

# NOTA: ya no copiamos data/ aca -- el docker-compose.yml monta
# ./data:/app/data como VOLUMEN, asi que se sincroniza en vivo con
# tu carpeta local, sin necesidad de reconstruir la imagen cada vez
# que cambia un CSV.

CMD ["tail", "-f", "/dev/null"]
## mantiene el contenedor vivo -- corres el .py a demanda con:
## docker exec -it src_container python mi_script_postgres.py