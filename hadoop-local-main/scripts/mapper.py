
#!/usr/bin/env python3
"""
Mapper de Hadoop Streaming: lee lineas de Venta.csv desde stdin,
y emite "idproducto<TAB>total_linea" para cada venta.
 
Sin f-strings (compatibilidad con Python 3.4/3.5, comun en imagenes
de Hadoop viejas como esta).
"""
import sys
 
for line in sys.stdin:
    line = line.strip()
 
    if not line or line.lower().startswith("idventa"):
        continue
 
    campos = line.split(",")
    if len(campos) < 10:
        continue
 
    id_producto = campos[7]
 
    try:
        precio = float(campos[8])
        cantidad = int(campos[9])
    except ValueError:
        continue
 
    total_linea = precio * cantidad
    print("%s\t%s" % (id_producto, total_linea))