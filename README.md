# Data Pipeline: Mundial 2026 ⚽

Proyecto integrador de la práctica: extracción, almacenamiento y
transformación de datos de fútbol usando Postgres, Python y dbt —
todo corriendo en contenedores Docker.

## Stack

- **Postgres** — base de datos donde viven los datos crudos y transformados
- **Python (extract)** — script que consulta la API de fútbol y carga datos crudos
- **dbt** — transforma los datos crudos en modelos limpios y agregados
- *(Próximamente)* **Airflow** — orquestación automática del pipeline completo
- *(Próximamente)* **GitHub Actions** — CI para validar cambios en cada Pull Request

## Estructura del proyecto

```
project-it/
├── docker-compose.yml
├── .env                      (no versionado — ver .env.example)
├── postgres/
│   └── data/                  (bind mount, no versionado)
├── src/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── extract_and_load.py
└── dbt/                        (próximo paso, todavía no creado)
    ├── dbt_project.yml
    ├── profiles/profiles.yml
    └── models/
        ├── staging/
        └── marts/
```

## Cómo levantar el proyecto

1. Copiar `.env.example` a `.env` y completar tu API key real
2. Levantar todo:
   ```bash
   docker compose up -d --build
   ```
3. Correr dbt (cuando esté sumado al proyecto):
   ```bash
   docker compose run --rm dbt run
   docker compose run --rm dbt test
   ```
4. Verificar datos:
   ```bash
   docker exec -it postgres_container psql -U db_user -d dbstgres -c "SELECT * FROM standings;"
   ```

## API utilizada

[API-Football](https://www.api-football.com/documentation-v3) — datos del Mundial (`league=1`). El plan gratuito solo da acceso a temporadas pasadas (usamos `season=2022` para desarrollo).

---

## 📓 Bitácora semanal

### Semana 1 — Fundamentos
- Levantamos Postgres con Docker Compose (bind mount para los datos)
- Practicamos el ciclo `stop`/`start` vs `down`/`up`, y qué pasa con los datos en cada caso
- Entendimos la diferencia entre bind mount y volumen con nombre

### Semana 2 — Extracción de datos
- Exploramos la API de fútbol con Postman (colección disponible en `/docs`)
- Armamos `extract_and_load.py`: extrae standings del Mundial e inserta en Postgres
- Resolvimos problemas de entorno Python (venv, versiones, `uv` vs `pip`)
- Containerizamos el script (`extract/Dockerfile`), ahora corre dentro de Docker, no en la máquina local

### Semana 3 — Transformación con dbt (próxima)
- Sumar el servicio `dbt` al compose (imagen oficial `dbt-postgres`)
- Crear el primer modelo de staging (`stg_standings`) y un mart (`mart_group_ranking`)
- Agregar tests básicos (`not_null`, `unique`)
-

### Semana 4 — (próxima)
-

### Semana 5 — (próxima)
-

### Semana 6 — (próxima)
-

---

## Decisiones de diseño (para recordar el "por qué")

- **Bind mount en vez de volumen con nombre para Postgres**: elegido a propósito para poder ver físicamente la carpeta de datos y entender mejor la persistencia
- **`extract` y `dbt` no quedan corriendo permanentemente**: son tareas puntuales (`run`/`up` una vez y terminan), a diferencia de `db` que corre todo el tiempo
- **Tabla `standings` simplificada** (`pais`, `puntos`, `mundial`, `grupo`): decisión consciente de simplicidad sobre un modelo más completo, para facilitar el aprendizaje inicial
- **Sin upsert todavía**: correr `extract` más de una vez genera duplicados — pendiente de resolver cuando se introduzca la lógica de `ON CONFLICT`

## Problemas conocidos / limitaciones actuales

- El plan gratuito de la API no da acceso a la temporada 2026 en curso — se usa 2022 para desarrollo
- Ejecutar el servicio de extracción más de una vez duplica filas en `standings`
- El script `.py` de extracción todavía no se probó corriendo *dentro* del contenedor (solo se validó desde el venv local)
- dbt todavía no está incorporado al proyecto — próximo paso
