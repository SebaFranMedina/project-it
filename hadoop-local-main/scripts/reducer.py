#!/usr/bin/env python3
"""
Reducer de Hadoop Streaming: suma el total por idproducto.
Sin f-strings, por compatibilidad.
"""
import sys

producto_actual = None
suma_actual = 0.0

for line in sys.stdin:
    partes = line.strip().split("\t")
    if len(partes) != 2:
        continue

    id_producto, total = partes
    total = float(total)

    if producto_actual == id_producto:
        suma_actual += total
    else:
        if producto_actual is not None:
            print("%s\t%s" % (producto_actual, suma_actual))
        producto_actual = id_producto
        suma_actual = total

if producto_actual is not None:
    print("%s\t%s" % (producto_actual, suma_actual))