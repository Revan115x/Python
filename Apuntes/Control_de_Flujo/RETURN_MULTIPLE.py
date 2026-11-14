# TEMA 3 - DEVOLVER MÚLTIPLES RESULTADOS

# --------------------------------------------------
# EJEMPLO 1: devolver varios resultados
# Python agrupa los valores devueltos en una tupla.
# --------------------------------------------------
def operar(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2

resultados = operar(5, 2)
print(resultados)

# Resultado:
# (7, 3, 10)


# --------------------------------------------------
# EJEMPLO 2: desempaquetar los resultados en variables
# El orden de las variables debe coincidir con el return.
# --------------------------------------------------
def operar(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2

suma, resta, producto = operar(5, 2)

print("Suma:", suma)
print("Resta:", resta)
print("Producto:", producto)

# Resultado:
# Suma: 7
# Resta: 3
# Producto: 10
