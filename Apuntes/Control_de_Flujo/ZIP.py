# TEMA 3 - RECORRER VARIAS SECUENCIAS CON ZIP

# --------------------------------------------------
# EJEMPLO 1: recorrer dos secuencias a la vez
# --------------------------------------------------
numeros = range(1, 5)
nombres = ["Ana", "Juan", "Pepe"]

for numero, nombre in zip(numeros, nombres):
    print(numero, nombre)

# Resultado:
# 1 Ana
# 2 Juan
# 3 Pepe
#
# El recorrido termina cuando se acaba la secuencia más corta.


# --------------------------------------------------
# EJEMPLO 2: relacionar productos y precios
# --------------------------------------------------
productos = ["Pan", "Leche", "Huevos"]
precios = [1.20, 0.95, 2.50]

for producto, precio in zip(productos, precios):
    print(producto, precio, "euros")

# Resultado:
# Pan 1.2 euros
# Leche 0.95 euros
# Huevos 2.5 euros
