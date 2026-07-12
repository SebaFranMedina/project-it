# Proyecto dbt

Transforma los datos crudos de `standings` (cargados por el servicio `src`)
en modelos limpios y agregados.

## Estructura

```
dbt/
├── Dockerfile              # imagen propia (dbt-core + dbt-postgres, arm64-friendly)
├── requirements.txt
├── dbt_project.yml
├── profiles/profiles.yml    # conexión a Postgres (host: db)
└── models/
    ├── staging/
    │   ├── sources.yml       # declara que "standings" ya existe (la carga "src")
    │   ├── schema.yml         # tests: unique, not_null
    │   └── stg_standings.sql  # limpia/expone la tabla cruda
    └── marts/
        └── mart_group_ranking.sql   # calcula el ranking por grupo
```



## Modelos


| Modelo               | Tipo  | Qué hace                                            |
| -------------------- | ----- | --------------------------------------------------- |
| `stg_standings`      | view  | Expone `standings` con nombres/tipos limpios        |
| `mart_group_ranking` | table | Calcula la posición de cada país dentro de su grupo |




## Comandos

```bash
docker compose run --rm dbt debug   # valida conexión
docker compose run --rm dbt run     # corre las transformaciones
docker compose run --rm dbt test    # corre los tests
```

