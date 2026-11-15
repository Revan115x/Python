"""
CHULETA PYTHON: LISTAS, INDICES, SLICING, APPEND Y EXTEND
Nivel: principiante

Este archivo sirve como chuleta de estudio.
Los ejemplos están comentados para que puedas entenderlos desde cero.
"""

# ============================================================
# 1. LISTAS
# ============================================================

# Una lista guarda varios elementos en una sola variable.
datos = ["DAW", 10, 20.5, ["Python", "Java", "C++"], True, "Salesianas"]

# Los índices empiezan en 0:
# índice 0 -> "DAW"
# índice 1 -> 10
# índice 2 -> 20.5
# índice 3 -> ["Python", "Java", "C++"]
# índice 4 -> True
# índice 5 -> "Salesianas"

# Una lista que está dentro de otra lista se llama lista anidada.


# ============================================================
# 2. ACCEDER A ELEMENTOS
# ============================================================

# Acceder a un elemento mediante su índice:
print(datos[0])       # "DAW"
print(datos[1])       # 10

# Índices negativos: empiezan a contar desde el final.
print(datos[-1])      # "Salesianas" (último elemento)
print(datos[-2])      # True (penúltimo elemento)

# Acceder a una lista interior y después a uno de sus elementos:
print(datos[3])       # ["Python", "Java", "C++"]
print(datos[3][1])    # "Java"


# ============================================================
# 3. SLICING: OBTENER UNA PARTE DE UNA LISTA
# ============================================================

# Sintaxis:
# lista[inicio:final:paso]
#
# inicio: posición desde la que empezamos.
# final: posición donde paramos, SIN incluirla.
# paso: cuántas posiciones avanzamos.

# Ejemplo:
numeros = [10, 20, 30, 40, 50]

print(numeros[1:3])   # [20, 30]
# Empieza en el índice 1 y termina antes del índice 3.

print(numeros[:3])    # [10, 20, 30]
# Si no indicamos inicio, empieza desde el principio.

print(numeros[2:])    # [30, 40, 50]
# Si no indicamos final, llega hasta el final.

print(numeros[::2])   # [10, 30, 50]
# Empieza desde el principio y avanza de dos en dos.

print(numeros[::-1])  # [50, 40, 30, 20, 10]
# Un paso de -1 recorre la lista al revés.


# ============================================================
# 4. RESOLUCIÓN DEL EJEMPLO DEL EJERCICIO
# ============================================================

datos = ["DAW", 10, 20.5, ["Python", "Java", "C++"], True, "Salesianas"]

p1 = datos[1:4]
print(p1)  # [10, 20.5, ["Python", "Java", "C++"]]

p2 = datos[3][1]
print(p2)  # "Java"

p3 = datos[-2:]
print(p3)  # [True, "Salesianas"]

p4 = datos[::2]
print(p4)  # ["DAW", 20.5, True]

# append() modifica la lista interior datos[3].
datos[3].append("SQL")

p5 = datos[3]
print(p5)  # ["Python", "Java", "C++", "SQL"]


# ============================================================
# 5. APPEND(): AÑADIR UN ELEMENTO
# ============================================================

# append() añade EXACTAMENTE lo que le pasamos como UN SOLO elemento.
# Si le pasamos una lista, esa lista queda dentro de la lista principal.

numeros = [1, 2]
numeros.append(3)
print(numeros)  # [1, 2, 3]

numeros = [1, 2]
numeros.append([3, 4])
print(numeros)  # [1, 2, [3, 4]]
# [3, 4] se añade como un único elemento: una lista dentro de otra lista.

# IMPORTANTE:
# append() no crea una lista nueva por sí solo.
# Añade el objeto que le pasamos al final de la lista existente.


# ============================================================
# 6. EXTEND(): AÑADIR VARIOS ELEMENTOS
# ============================================================

# extend() recorre la colección que le pasamos y añade sus elementos
# individualmente a la lista principal.

numeros = [1, 2]
numeros.extend([3, 4])
print(numeros)  # [1, 2, 3, 4]

numeros = [1, 2]
numeros.extend([3])
print(numeros)  # [1, 2, 3]

# En este caso NO queda una lista dentro de otra.


# ============================================================
# 7. COMPARACIÓN: APPEND() VS EXTEND()
# ============================================================

# Partimos de la misma lista en cada ejemplo:

# append([3, 4])
# [1, 2, [3, 4]]
# Añade la lista completa como un solo elemento.

# extend([3, 4])
# [1, 2, 3, 4]
# Añade los elementos de la lista por separado.

# append(3)
# [1, 2, 3]
# Añade el número 3 como un elemento.

# extend([3])
# [1, 2, 3]
# Añade el único elemento que contiene la lista [3].


# ============================================================
# 8. TRUCOS PARA EL EXAMEN
# ============================================================

# 1. Los índices empiezan en 0.
# 2. El índice -1 es el último elemento.
# 3. En un slicing, el índice final NO se incluye.
# 4. [::2] significa avanzar de dos en dos.
# 5. [::-1] devuelve los elementos en orden inverso.
# 6. lista[3][1] significa: entra en el elemento 3 y accede
#    al elemento 1 de la lista interior.
# 7. append() añade un objeto como un único elemento.
# 8. extend() añade individualmente los elementos de una colección.
# 9. append() y extend() modifican la lista original.

# FIN DE LA CHULETA
