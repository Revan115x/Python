# TEMA 3 - FUNCIONES

# --------------------------------------------------
# EJEMPLO 1: definir y llamar una función sin parámetros
# --------------------------------------------------
def saludar():
    print("Hola, bienvenido")

saludar()

# Resultado:
# Hola, bienvenido


# --------------------------------------------------
# EJEMPLO 2: función con parámetros
# --------------------------------------------------
def mostrar_nombre(nombre):
    print("Hola", nombre)

mostrar_nombre("Ana")
mostrar_nombre("Juan")

# Resultado:
# Hola Ana
# Hola Juan


# --------------------------------------------------
# EJEMPLO 3: función que devuelve un resultado con return
# --------------------------------------------------
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(4, 5)
print(total)

# Resultado:
# 9


# --------------------------------------------------
# EJEMPLO 4: factorial como en los apuntes
# --------------------------------------------------
def factorial(n):
    """Calcula el factorial de un número no negativo."""
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado

print(factorial(5))

# Resultado:
# 120
