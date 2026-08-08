# Hadoop - Apuntes Teóricos

## ¿Qué es Hadoop?

Apache Hadoop es un ecosistema de herramientas diseñado para almacenar y procesar grandes volúmenes de datos de forma distribuida sobre un conjunto de servidores (cluster).

Su principal ventaja es que permite trabajar con datasets que no caben en un único ordenador, repartiendo tanto el almacenamiento como el procesamiento entre varias máquinas.

---

# Conceptos básicos

## Cluster

Un **cluster** es un conjunto de ordenadores que trabajan como si fueran uno solo.

Ejemplo:

```
             Cluster Hadoop

+-----------+    +-----------+    +-----------+
| Máquina 1 |    | Máquina 2 |    | Máquina 3 |
+-----------+    +-----------+    +-----------+
```

Cada máquina recibe el nombre de **Nodo (Node)**.

---



# Arquitectura de Hadoop

Tradicionalmente se hablaba de una arquitectura **Master-Slave** (hoy suele utilizarse la terminología **Manager-Worker**).

```
                    MASTER

           +-----------------------+
           |      NameNode         |
           |   ResourceManager     |
           +----------+------------+
                      |
      ---------------------------------------
      |             |             |          |
      ▼             ▼             ▼          ▼

 +------------+ +------------+ +------------+ +------------+
 | Worker 1   | | Worker 2   | | Worker 3   | | Worker 4   |
 |------------| |------------| |------------| |------------|
 | DataNode   | | DataNode   | | DataNode   | | DataNode   |
 |NodeManager | |NodeManager | |NodeManager | |NodeManager |
 +------------+ +------------+ +------------+ +------------+
```

---



# Master

El Master coordina todo el cluster.

Normalmente ejecuta dos servicios principales:

- NameNode
- ResourceManager

---



## NameNode

Es el cerebro del sistema de archivos HDFS.

No almacena los datos.

Almacena únicamente la información sobre dónde están los datos.

Ejemplo:

```
Ventas.csv

↓

Bloque 1 → Worker 1
Bloque 2 → Worker 3
Bloque 3 → Worker 2
```

Es decir:

- conoce todos los archivos
- conoce todos los bloques
- conoce en qué nodo está cada bloque

---



## ResourceManager

Forma parte de YARN.

Su trabajo consiste en administrar los recursos del cluster.

Decide:

- qué nodo tiene memoria disponible
- qué nodo tiene CPU libre
- dónde ejecutar un proceso

No procesa datos.

Simplemente coordina.

---



# Workers

Cada Worker contiene normalmente dos procesos importantes.

## DataNode

Es quien almacena físicamente los datos.

Ejemplo:

```
Worker 1

Bloque 1
Bloque 5
Bloque 9
```

---



## NodeManager

Es el encargado de ejecutar los procesos enviados por YARN.

Cuando Spark o MapReduce necesita ejecutar una tarea:

```
ResourceManager

↓

NodeManager

↓

Ejecuta el proceso
```

---



# HDFS

HDFS significa:

**Hadoop Distributed File System**

Es un sistema de archivos distribuido.

Su objetivo es almacenar archivos enormes repartidos entre muchas máquinas.

---



## ¿Cómo funciona?

Supongamos un archivo:

```
Ventas.csv (900 GB)
```

HDFS lo divide automáticamente.

```
Bloque 1
Bloque 2
Bloque 3
...
Bloque 900
```

Después reparte esos bloques entre todos los Workers.

Ejemplo:

```
Worker 1

Bloque 1
Bloque 4
Bloque 7

-------------------

Worker 2

Bloque 2
Bloque 5
Bloque 8

-------------------

Worker 3

Bloque 3
Bloque 6
Bloque 9
```

---



# Replicación

Una de las grandes ventajas de HDFS es la tolerancia a fallos.

Cada bloque suele almacenarse tres veces.

Ejemplo:

```
Bloque 2

Worker 2

Worker 4

Worker 5
```

Si un servidor falla, otra copia sigue disponible.

El usuario ni siquiera nota el fallo.

---



# YARN

YARN significa:

**Yet Another Resource Negotiator**

Es el sistema encargado de administrar todos los recursos del cluster.

Gestiona:

- CPU
- Memoria
- Procesos
- Prioridades

No procesa datos.

Simplemente decide dónde ejecutar cada tarea.

---



# MapReduce

MapReduce fue el primer sistema de procesamiento de Hadoop.

Consta de dos fases.

---



## MAP

Cada Worker procesa únicamente los datos que tiene almacenados.

Ejemplo:

```
Worker 1

Ventas Barcelona

↓

1200 €

--------------------

Worker 2

Ventas Madrid

↓

900 €

--------------------

Worker 3

Ventas Sevilla

↓

700 €
```

---



## REDUCE

Recoge todos los resultados parciales.

Los combina.

Obtiene el resultado final.

```
1200

+

900

+

700

↓

2800 €
```

---



# Flujo completo de Hadoop

```
Archivo CSV

↓

HDFS

↓

Map

↓

Reduce

↓

Resultado
```

---



# Ecosistema Hadoop

Hadoop no es únicamente HDFS.

Existen muchas herramientas.


| Herramienta | Función                                       |
| ----------- | --------------------------------------------- |
| HDFS        | Almacenamiento distribuido                    |
| YARN        | Gestión de recursos                           |
| MapReduce   | Procesamiento distribuido                     |
| Hive        | SQL sobre Hadoop                              |
| Pig         | Transformación de datos                       |
| HBase       | Base de datos NoSQL                           |
| Sqoop       | Importar datos desde bases relacionales       |
| Flume       | Ingesta de logs                               |
| Oozie       | Orquestación de procesos                      |
| Spark       | Procesamiento distribuido de alto rendimiento |


---



# Hadoop vs Spark


| Hadoop (MapReduce) | Spark                                |
| ------------------ | ------------------------------------ |
| Procesa en disco   | Procesa principalmente en memoria    |
| Más lento          | Mucho más rápido                     |
| Batch              | Batch + Streaming + Machine Learning |
| Más antiguo        | Estándar actual                      |


Actualmente es muy habitual utilizar:

- HDFS para almacenar
- Spark para procesar
- Hive para consultar mediante SQL

---



# ¿Qué ocurre cuando ejecutamos una consulta?

Ejemplo:

```sql
SELECT SUM(Precio)
FROM Venta;
```

El flujo sería:

```
Usuario

↓

ResourceManager

↓

Worker 1 procesa Bloque 1

Worker 2 procesa Bloque 2

Worker 3 procesa Bloque 3

↓

Se combinan todos los resultados

↓

Resultado final
```

Cada Worker trabaja simultáneamente.

Por eso Hadoop escala tan bien.

---



# Relación con un ETL tradicional

Actualmente nuestro proyecto realiza este flujo:

```
CSV

↓

Python (Pandas)

↓

PostgreSQL
```

Todo ocurre en una única máquina.

En un entorno Big Data el flujo sería:

```
CSV

↓

HDFS

↓

Spark

↓

Hive / Data Warehouse
```

La idea es exactamente la misma.

La diferencia es que ahora el procesamiento se realiza entre decenas o cientos de servidores.

---



# Relación con nuestro proyecto

Actualmente ya estamos utilizando varios conceptos propios de un pipeline de datos:

- Docker
- PostgreSQL
- Python
- Pandas
- SQL
- ETL

Más adelante simplemente sustituiremos algunas piezas:


| Proyecto actual | Big Data              |
| --------------- | --------------------- |
| Carpeta `data/` | HDFS                  |
| Pandas          | Spark                 |
| `load_data.py`  | Spark Jobs            |
| PostgreSQL      | Hive / Data Warehouse |
| Docker Compose  | Cluster Hadoop        |


La filosofía sigue siendo exactamente la misma:

1. Obtener datos.
2. Transformarlos.
3. Cargarlos.
4. Consultarlos.
5. Escalar el procesamiento cuando el volumen crece.

