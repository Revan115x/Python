# 11 - Formateo de cadenas: estilo antiguo y format()

# Estilo antiguo con %
print("%d %f %s" % (2.5, 2.5, 2.5))
print("Producto %s, cantidad=%d, precio=%.2f" % ("cesta", 23, 13.456))

# Metodo format: marcadores por orden.
print("Un {} vale {} {}".format("€", 1.12, "$"))

# Indicando posiciones.
print("Un {2} vale {1} {0}".format("€", 1.12, "$"))

# Utilizando nombres.
print("Un {moneda1} vale {cambio} {moneda2}".format(
    moneda1="€", cambio=1.12, moneda2="$"
))

# Alineacion y anchura.
print("|{:<10}|".format("lunes"))  # izquierda
print("|{:>10}|".format("lunes"))  # derecha
print("|{:^10}|".format("lunes"))  # centro

# Formato numerico: anchura y decimales.
print("Cantidad {:5d}".format(12))
print("Pi vale {:8.4f}".format(3.141592))
