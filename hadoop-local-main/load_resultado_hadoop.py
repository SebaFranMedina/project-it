"""
Carga el resultado del job de Hadoop (total vendido por producto)
en una tabla nueva de Postgres: resumen_ventas_hadoop.

Correr DESPUÉS de traer el archivo de resultado desde HDFS a tu Mac
(ver comandos en el README que acompaña este script).
"""
import csv
import psycopg2

RUTA_RESULTADO = "data/resultado_ventas_por_producto.tsv"

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'playground',
    'user': 'postgres',
    'password': '******' # contraseña de la base de datos
}


def cargar_resultado():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS resumen_ventas_hadoop (
            id_producto INTEGER PRIMARY KEY,
            total_vendido NUMERIC
        );
    """)
    cur.execute("TRUNCATE TABLE resumen_ventas_hadoop;")

    filas_cargadas = 0
    with open(RUTA_RESULTADO) as f:
        reader = csv.reader(f, delimiter="\t")
        for id_producto, total in reader:
            cur.execute(
                "INSERT INTO resumen_ventas_hadoop (id_producto, total_vendido) VALUES (%s, %s)",
                (int(id_producto), float(total))
            )
            filas_cargadas += 1

    conn.commit()
    cur.close()
    conn.close()
    print(f"{filas_cargadas} productos cargados en 'resumen_ventas_hadoop'")


if __name__ == "__main__":
    cargar_resultado()
