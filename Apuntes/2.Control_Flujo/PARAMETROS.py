# TEMA 3 - PARÁMETROS Y ARGUMENTOS

# --------------------------------------------------
# EJEMPLO 1: argumentos posicionales
# El primer argumento corresponde al primer parámetro.
# --------------------------------------------------
def presentar(nombre, edad):
    print(nombre, edad)

presentar("Ana", 20)

# Resultado:
# Ana 20


# --------------------------------------------------
# EJEMPLO 2: parámetros con valor por defecto
# Si no indicamos saludo, se utiliza "Hola".
# --------------------------------------------------
def saludar(nombre, saludo="Hola"):
    print(saludo, nombre)

saludar("Ana")
saludar("Juan", "Buenos días")

# Resultado:
# Hola Ana
# Buenos días Juan


# --------------------------------------------------
# EJEMPLO 3: argumentos con nombre (keyword arguments)
# Podemos indicar el nombre de cada parámetro.
# --------------------------------------------------
def presentar_persona(nombre, edad):
    print(nombre, edad)

presentar_persona(edad=20, nombre="Ana")

# Resultado:
# Ana 20


# --------------------------------------------------
# EJEMPLO 4: ejemplo de operar basado en los apuntes
# --------------------------------------------------
def operar(n1, n2, operador="+", respuesta="El resultado es "):
    if operador == "+":
        return respuesta + str(n1 + n2)
    elif operador == "-":
        return respuesta + str(n1 - n2)
    else:
        return "Error"

print(operar(5, 7))
print(operar(4, 6, respuesta="La suma es "))
print(operar(4, 6, respuesta="La resta es ", operador="-"))

# Resultado:
# El resultado es 12
# La suma es 10
# La resta es -2
