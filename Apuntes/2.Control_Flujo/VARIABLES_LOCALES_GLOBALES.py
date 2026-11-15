# TEMA 3 - VARIABLES LOCALES Y GLOBALES

# --------------------------------------------------
# EJEMPLO 1: variable local
# La variable resta existe dentro de la función.
# --------------------------------------------------
def operar(a, b):
    suma = a + b
    resta = a - b
    print(suma, resta)

operar(4, 5)

# Resultado:
# 9 -1

# Si intentamos hacer print(resta) fuera de la función,
# Python dará NameError porque resta es una variable local.


# --------------------------------------------------
# EJEMPLO 2: consultar una variable global
# --------------------------------------------------
PI = 3.1415

def area(radio):
    return PI * radio ** 2

print(area(2))

# Resultado:
# 12.566


# --------------------------------------------------
# EJEMPLO 3: modificar una variable global con global
# --------------------------------------------------
suma = 0

def calcular(a, b):
    global suma
    suma = a + b

calcular(4, 5)
print(suma)

# Resultado:
# 9
