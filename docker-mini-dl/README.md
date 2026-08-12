# Mini Data Lake + Data Warehouse

Proyecto educativo de Ingeniería de Datos utilizando Docker, Jupyter,
MinIO, PostgreSQL y una API externa.

El objetivo es construir un pipeline completo desde la ingesta de datos
hasta su consumo analítico.

## 1. Arquitectura

API / CSV
   │
   ▼
RAW
JSON / CSV
   │
   ▼
BRONZE
Parquet
   │
   ▼
SILVER
Datos limpios y estructurados
   │
   ▼
GOLD
Modelo analítico
   │
   ▼
PostgreSQL
   │
   ▼
SQL / BI / Analytics

## 2. Servicios

El proyecto utiliza Docker Compose para levantar:

- Jupyter
- MinIO
- PostgreSQL
- Adminer

### Jupyter

Entorno de trabajo para ejecutar los notebooks.

Puerto:

```
http://localhost:8888
```

Token configurado:

```
profesor
```



### MinIO

Data Lake / almacenamiento de objetos.

API:

```
http://localhost:9000
```

Consola:

```
http://localhost:9001
```

Credenciales iniciales:

```
Usuario: minioadmin
Password: minioadmin
```



### PostgreSQL

Base de datos / Data Warehouse.

Puerto:

```
5432
```

Base de datos:

```
dw
```

Usuario:

```
postgres
```

Password:

```
postgres
```



### Adminer

Interfaz web para administrar PostgreSQL.

```
http://localhost:8080
```



## 3. Estructura del proyecto

```
.
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
│
├── datasets/
│   └── raw/
│
├── notebooks/
│   ├── 01_generate_sales.ipynb
│   ├── 02_upload_raw.ipynb
│   ├── 03_bronze.ipynb
│   ├── 04_silver.ipynb
│   ├── 05_gold.ipynb
│   └── 06_load_postgres.ipynb
│
├── src/
│   ├── generators/
│   │   └── sales.py
│   │
│   └── storage/
│       └── minio_client.py
│
└── sql/
    └── 01_create_tables.sql
```



## 4. Levantar el proyecto

Desde la raíz del proyecto:

```
docker compose up -d
```

Comprobar los contenedores:

```
docker compose ps
```

Ver logs:

```
docker compose logs
```

Detener los servicios:

```
docker compose stop
```

Eliminar los contenedores:

```
docker compose down
```



## 5. MinIO

Crear los buckets:

```
raw
bronze
silver
gold
```

La estructura conceptual será:

```
MinIO
│
├── raw/
├── bronze/
├── silver/
└── gold/
```



## 6. RAW

Raw representa los datos tal como llegan desde la fuente.

Ejemplo con una API:

```
API
 ↓
JSON
 ↓
raw/networks.json
```

No realizamos transformaciones de negocio en Raw.

El objetivo es conservar una representación cercana a la fuente original.

## 7. BRONZE

Bronze transforma los datos a un formato eficiente para procesamiento.

Ejemplo:

```
raw/networks.json
        ↓
     DataFrame
        ↓
   networks.parquet
        ↓
bronze/networks.parquet
```

La principal transformación realizada en este proyecto es:

```
JSON / CSV → Parquet
```

Bronze todavía conserva la estructura de los datos de origen siempre
que sea posible.

## 8. SILVER

Silver contiene datos limpios, tipados y estructurados.

Aquí se realizan operaciones como:

- limpieza de columnas
- normalización de tipos
- tratamiento de valores nulos
- eliminación de duplicados
- transformación de estructuras anidadas
- normalización de arrays/listas

Ejemplo:

```
Bronze
   ↓
limpieza
   ↓
Silver
```



## 9. GOLD

Gold representa los datos preparados para consumo analítico.

En este proyecto se construye un pequeño modelo dimensional:

```
dim_city
dim_system
fact_network
```

Conceptualmente:

```
            dim_city
                │
                │
                ▼
          fact_network
                ▲
                │
            dim_system
```

El grano de fact_network es:

```
Una fila = una red de bicicletas.
```



## 10. Gold → PostgreSQL

Los Parquet de Gold se almacenan inicialmente en MinIO:

```
gold/
├── dim_city.parquet
├── dim_system.parquet
└── fact_network.parquet
```

Posteriormente se cargan en PostgreSQL.

La creación de las tablas se realiza mediante SQL.

La carga de los datos se realiza desde Jupyter.

## 11. PostgreSQL

El modelo contiene:

```
dim_city
dim_system
fact_network
```

La tabla fact_network mantiene relaciones mediante claves foráneas:

```
fact_network.city_key
        ↓
dim_city.city_key

fact_network.system_key
        ↓
dim_system.system_key
```



## 12. Flujo completo

```
Fuente
  │
  ▼
RAW
  │
  ▼
BRONZE
  │
  ▼
SILVER
  │
  ▼
GOLD
  │
  ▼
PostgreSQL
  │
  ▼
SQL / Analytics
```



## 13. Detener el proyecto

Para detener los servicios sin eliminar los datos:

```
docker compose stop
```

Para detener y eliminar los contenedores:

```
docker compose down
```

Para eliminar también los volúmenes:

```
docker compose down -v
```

ATENCIÓN:

`docker compose down -v` elimina los volúmenes de PostgreSQL y MinIO
y, por tanto, los datos persistidos.

## 14. Dependencias

Las dependencias Python del proyecto se mantienen en:

```
requirements.txt
```

El Dockerfile instala estas dependencias al construir la imagen
personalizada de Jupyter.

Esto evita depender de las librerías que casualmente incluya la imagen
base de Jupyter.

## 15. Principio de diseño

Cada capa tiene una responsabilidad diferente:

RAW:
    conservar la fuente.

BRONZE:
    almacenar eficientemente en Parquet.

SILVER:
    limpiar y estructurar.

GOLD:
    preparar para analítica.

POSTGRES:
    servir los datos para consumo SQL / BI.