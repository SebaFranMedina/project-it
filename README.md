# Curso de Ingeniería de Datos

Material práctico construido a lo largo del curso, con foco en
**Postgres, cargas incrementales, diseño de pipelines ETL, Docker
(como eje central), Hadoop y arquitecturas de data lake**.

A lo largo de las clases se trabajó de forma incremental: desde levantar
una base de datos en un contenedor, hasta diseñar un pipeline ETL
completo con cargas incrementales e idempotentes, transformaciones con
dbt y PySpark, un caso de procesamiento distribuido con Hadoop
(HDFS + MapReduce), y los primeros pasos hacia una arquitectura de data
lake moderna (Iceberg + MinIO). Todo containerizado con Docker, que
funcionó como el hilo conductor de cada etapa del curso.

## Temas cubiertos

- **Docker**: contenedores, imágenes, volúmenes, redes, `docker-compose`, multi-servicio
- **Postgres**: modelado, DDL, conexión desde Python, `psql`, administración básica
- **Pipelines ETL**: extracción desde APIs y CSVs, transformación con reglas de negocio, carga con `upsert` y control de duplicados
- **Cargas incrementales**: detección de archivos nuevos, archivado de procesados, idempotencia, columnas de auditoría (`created_at`/`updated_at`)
- **dbt**: modelos, tests, staging y marts
- **PySpark**: transformaciones distribuidas, Window Functions, buenas prácticas de producción
- **SQL avanzado**: integridad referencial, detección de anomalías, auditoría de pipelines
- **Hadoop**: HDFS, MapReduce con Hadoop Streaming, procesamiento distribuido
- **Data Lake**: arquitectura Medallion, Iceberg, almacenamiento tipo S3 con MinIO
- **Git/GitHub**: ramas, forks, flujo colaborativo

---

*Material elaborado por* **Mauro Nicolás Pérez**
📧 [mauro.nperez@gmail.com](mailto:mauro.nperez@gmail.com)