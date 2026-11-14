# TEMA 3 - ARGUMENTOS ARBITRARIOS: *args Y **kwargs

# --------------------------------------------------
# EJEMPLO 1: *args
# Recibe varios argumentos posicionales.
# Dentro de la función, args se comporta como una tupla.
# --------------------------------------------------
def sumar(*args):
    resultado = 0

    for numero in args:
        resultado += numero

    return resultado

print(sumar(2))
print(sumar(2, 3, 4))
print(sumar(1, 2, 3, 4, 5))

# Resultado:
# 2
# 9
# 15


# --------------------------------------------------
# EJEMPLO 2: **kwargs
# Recibe varios argumentos con nombre.
# Dentro de la función, kwargs se comporta como un diccionario.
# --------------------------------------------------
def mostrar_datos(**kwargs):
    for clave, valor in kwargs.items():
        print(clave, valor)

mostrar_datos(nombre="Ana", edad=20, ciudad="Madrid")

# Resultado:
# nombre Ana
# edad 20
# ciudad Madrid
