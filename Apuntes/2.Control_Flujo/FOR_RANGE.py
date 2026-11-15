# TEMA 3 - BUCLE FOR Y RANGE

# --------------------------------------------------
# EJEMPLO 1: range con un argumento
# Empieza en 0 y llega hasta el número anterior.
# --------------------------------------------------
for i in range(5):
    print(i)

# Resultado:
# 0
# 1
# 2
# 3
# 4


# --------------------------------------------------
# EJEMPLO 2: range con inicio y final
# El final no se incluye.
# --------------------------------------------------
for i in range(1, 5):
    print(i)

# Resultado:
# 1
# 2
# 3
# 4


# --------------------------------------------------
# EJEMPLO 3: for recorriendo una cadena
# --------------------------------------------------
nombre = "ANA"

for letra in nombre:
    print(letra)

# Resultado:
# A
# N
# A


# --------------------------------------------------
# EJEMPLO 4: for recorriendo una lista
# --------------------------------------------------
nombres = ["Ana", "Juan", "Pepe"]

for nombre in nombres:
    print(nombre)

# Resultado:
# Ana
# Juan
# Pepe


# --------------------------------------------------
# EJEMPLO 5: for con else
# --------------------------------------------------
for numero in range(1, 4):
    print(numero)
else:
    print("Hemos terminado")

# Resultado:
# 1
# 2
# 3
# Hemos terminado
