"""
CHULETA DE EXAMEN: DICCIONARIOS EN PYTHON (dict)
DAW - Explicado desde cero y con ejemplos para copiar y adaptar.

OBJETIVO
--------
Que puedas consultar este archivo cuando te quedes atascado:
- Crear diccionarios de distintas maneras.
- Mostrar datos y recorrer claves, valores y parejas.
- Añadir, modificar y eliminar.
- Buscar claves sin provocar errores.
- Crear diccionarios a partir de listas y tuplas.
- Contar elementos y agrupar información.
- Trabajar con diccionarios que contienen listas u otros diccionarios.
- Resolver ejercicios típicos de examen.

IMPORTANTE
----------
1. Un diccionario guarda parejas CLAVE: VALOR.
2. Se accede mediante la clave: diccionario["nombre"].
3. Las claves no se repiten.
4. Los valores sí pueden repetirse.
5. Un diccionario se puede modificar.
6. Al recorrerlo directamente, se recorren sus CLAVES.
7. {} crea un diccionario vacío. set() crea un conjunto vacío.

Los resultados aparecen en comentarios o en print().
"""

print("=" * 78)
print("CHULETA COMPLETA DE DICCIONARIOS")
print("=" * 78)


# =============================================================================
# 1. ENTENDER QUÉ ES UNA CLAVE Y QUÉ ES UN VALOR
# =============================================================================

# En este ejemplo:
# "nombre", "edad" y "ciudad" son las CLAVES.
# "Ana", 20 y "Madrid" son los VALORES.

persona = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Madrid"
}

print("\n1. Diccionario completo:")
print(persona)
# {'nombre': 'Ana', 'edad': 20, 'ciudad': 'Madrid'}

# Para obtener un valor, escribimos su clave entre corchetes.
print(persona["nombre"])  # Ana
print(persona["edad"])    # 20

# PIENSA ASÍ:
# persona["nombre"]
#     |       |
# diccionario clave que busco
#
# Python busca la clave "nombre" y devuelve su valor "Ana".


# =============================================================================
# 2. TODAS LAS FORMAS IMPORTANTES DE CREAR UN DICCIONARIO
# =============================================================================

# FORMA 1: con llaves { }.
alumno1 = {
    "nombre": "Luis",
    "edad": 22
}

# FORMA 2: con dict().
alumno2 = dict(nombre="Marta", edad=21)

# FORMA 3: diccionario vacío.
alumno3 = {}
alumno4 = dict()

# FORMA 4: desde una lista de tuplas.
# Cada tupla tiene exactamente dos elementos: (clave, valor).
parejas = [
    ("España", "Madrid"),
    ("Francia", "París"),
    ("Italia", "Roma")
]
capitales1 = dict(parejas)

# FORMA 5: desde una lista de listas.
parejas2 = [
    ["Python", "Lenguaje"],
    ["HTML", "Marcado"],
    ["CSS", "Estilos"]
]
tipos = dict(parejas2)

# FORMA 6: desde DOS LISTAS relacionadas utilizando zip().
paises = ["España", "Francia", "Italia"]
capitales = ["Madrid", "París", "Roma"]

capitales2 = dict(zip(paises, capitales))

# FORMA 7: crear varias claves con el mismo valor.
claves = ["nombre", "edad", "ciudad"]
datos_vacios = dict.fromkeys(claves, "Pendiente")

print("\n2. Diferentes creaciones:")
print(alumno1)
print(alumno2)
print(alumno3)       # {}
print(capitales1)
print(tipos)
print(capitales2)
print(datos_vacios)

# EXPLICACIÓN DE zip():
# zip(paises, capitales) empareja los elementos que están en la misma posición:
# ("España", "Madrid")
# ("Francia", "París")
# ("Italia", "Roma")
#
# dict() convierte esas parejas en claves y valores.
#
# OJO: zip() se detiene cuando se termina la lista más corta.


# =============================================================================
# 3. MOSTRAR UN DICCIONARIO
# =============================================================================

persona = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Madrid"
}

# Mostrar el diccionario entero.
print("\n3. Mostrar todo:")
print(persona)

# Mostrar solamente un valor.
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Ciudad:", persona["ciudad"])

# Mostrar una frase utilizando los valores.
print(persona["nombre"], "tiene", persona["edad"], "años.")
# Ana tiene 20 años.


# =============================================================================
# 4. RECORRER UN DICCIONARIO: LAS 4 FORMAS QUE DEBES DOMINAR
# =============================================================================

datos = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Sevilla"
}

# ---------------------------------------------------------------------------
# FORMA 1. Recorrer directamente el diccionario.
# Esto recorre SOLAMENTE LAS CLAVES.
# ---------------------------------------------------------------------------

print("\n4.1 Recorrer directamente: claves")
for clave in datos:
    print(clave)

# Resultado:
# nombre
# edad
# ciudad

# ---------------------------------------------------------------------------
# FORMA 2. Recorrer con keys().
# También recorre las CLAVES.
# ---------------------------------------------------------------------------

print("\n4.2 Recorrer con keys():")
for clave in datos.keys():
    print(clave)

# Resultado:
# nombre
# edad
# ciudad

# ---------------------------------------------------------------------------
# FORMA 3. Recorrer con values().
# Recorre SOLAMENTE LOS VALORES.
# ---------------------------------------------------------------------------

print("\n4.3 Recorrer con values():")
for valor in datos.values():
    print(valor)

# Resultado:
# Carlos
# 25
# Sevilla

# ---------------------------------------------------------------------------
# FORMA 4. Recorrer con items().
# Permite obtener CLAVE Y VALOR a la vez.
# ---------------------------------------------------------------------------

print("\n4.4 Recorrer con items():")
for clave, valor in datos.items():
    print(clave, "->", valor)

# Resultado:
# nombre -> Carlos
# edad -> 25
# ciudad -> Sevilla

# CHULETA PARA ELEGIR:
#
# ¿Me piden mostrar las claves?
#     for clave in diccionario:
#         print(clave)
#
# ¿Me piden mostrar los valores?
#     for valor in diccionario.values():
#         print(valor)
#
# ¿Me piden mostrar cada clave junto a su valor?
#     for clave, valor in diccionario.items():
#         print(clave, valor)
#
# ERROR TÍPICO:
#     for clave, valor in diccionario:
#         ...
# Esto no es la forma correcta de obtener las parejas.
# Utiliza diccionario.items().


# =============================================================================
# 5. ACCEDER A UNA CLAVE: CORCHETES [] O get()
# =============================================================================

producto = {
    "nombre": "Teclado",
    "precio": 25.99
}

# OPCIÓN A: corchetes.
print("\n5. Acceso con corchetes:")
print(producto["nombre"])  # Teclado

# Si la clave no existe, se produce KeyError.
# print(producto["marca"])  # NO ejecutar: la clave no existe.

# OPCIÓN B: get().
print("\n5. Acceso con get():")
print(producto.get("nombre"))  # Teclado

# Si no existe, get() devuelve None.
print(producto.get("marca"))   # None

# Podemos indicar qué queremos que devuelva si no existe.
print(producto.get("marca", "Marca desconocida"))
# Marca desconocida

# DIFERENCIA:
# producto["marca"]                  -> KeyError.
# producto.get("marca")              -> None.
# producto.get("marca", "No existe") -> No existe.

# ¿CUÁL UTILIZO?
# - Si sé que la clave existe: diccionario["clave"].
# - Si puede que no exista: diccionario.get("clave").


# =============================================================================
# 6. COMPROBAR SI EXISTE UNA CLAVE: in / not in
# =============================================================================

persona = {
    "nombre": "Lucía",
    "edad": 19
}

print("\n6. Comprobar claves:")
print("nombre" in persona)       # True
print("telefono" in persona)     # False
print("telefono" not in persona) # True

# IMPORTANTE:
# in sobre un diccionario comprueba las CLAVES, no los valores.
print("Lucía" in persona)  # False

# Para comprobar si un valor existe:
print("Lucía" in persona.values())  # True

# Ejemplo práctico para evitar KeyError:
clave = "telefono"

if clave in persona:
    print(persona[clave])
else:
    print("La clave no existe")
# La clave no existe


# =============================================================================
# 7. AÑADIR Y MODIFICAR ELEMENTOS
# =============================================================================

alumno = {
    "nombre": "Ana",
    "edad": 20
}

# AÑADIR:
# Si la clave no existe, Python la crea.
alumno["ciudad"] = "Madrid"

# MODIFICAR:
# Si la clave ya existe, cambia el valor anterior.
alumno["edad"] = 21

# MODIFICAR UTILIZANDO EL VALOR ANTERIOR:
alumno["edad"] = alumno["edad"] + 1
# También se puede escribir: alumno["edad"] += 1

print("\n7. Añadir y modificar:")
print(alumno)
# {'nombre': 'Ana', 'edad': 22, 'ciudad': 'Madrid'}

# RECUERDA:
# diccionario["clave"] = valor
# - clave nueva: añade.
# - clave existente: modifica.


# =============================================================================
# 8. update(): AÑADIR O MODIFICAR VARIAS PAREJAS
# =============================================================================

persona = {
    "nombre": "Luis",
    "edad": 22
}

# Añade "ciudad" y modifica "edad".
persona.update({
    "edad": 23,
    "ciudad": "Valencia"
})

print("\n8. Después de update():")
print(persona)
# {'nombre': 'Luis', 'edad': 23, 'ciudad': 'Valencia'}

# También podemos pasar una lista de tuplas.
persona.update([
    ("curso", "DAW"),
    ("grupo", "A")
])

print(persona)

# update() modifica el diccionario original.
# No crea otro diccionario.


# =============================================================================
# 9. setdefault(): AÑADIR SOLO SI LA CLAVE NO EXISTE
# =============================================================================

persona = {
    "nombre": "Ana"
}

# "nombre" ya existe: no lo cambia.
resultado1 = persona.setdefault("nombre", "Luis")

# "edad" no existe: la añade con valor 20.
resultado2 = persona.setdefault("edad", 20)

print("\n9. setdefault():")
print(resultado1)  # Ana
print(resultado2)  # 20
print(persona)      # {'nombre': 'Ana', 'edad': 20}

# DIFERENCIA CON update():
# setdefault("nombre", "Luis"):
#     Si nombre existe, conserva el valor que tenía.
#
# persona["nombre"] = "Luis":
#     Cambia el valor siempre.
#
# persona.update({"nombre": "Luis"}):
#     También cambia el valor si ya existía.


# =============================================================================
# 10. ELIMINAR ELEMENTOS: pop(), popitem(), del y clear()
# =============================================================================

datos = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Madrid"
}

# ---------------------------------------------------------------------------
# pop(clave): elimina esa pareja y DEVUELVE su valor.
# ---------------------------------------------------------------------------

edad_eliminada = datos.pop("edad")

print("\n10. pop():")
print("Valor eliminado:", edad_eliminada)  # 20
print("Diccionario:", datos)

# Si la clave puede no existir, añade un valor por defecto:
telefono = datos.pop("telefono", "No había teléfono")
print(telefono)  # No había teléfono

# ---------------------------------------------------------------------------
# del: elimina la pareja, pero NO devuelve el valor.
# ---------------------------------------------------------------------------

del datos["ciudad"]
print("\nDespués de del:", datos)

# ---------------------------------------------------------------------------
# popitem(): elimina y devuelve la última pareja insertada.
# Devuelve una tupla: (clave, valor).
# ---------------------------------------------------------------------------

pareja_eliminada = datos.popitem()
print("\npopitem devuelve:", pareja_eliminada)
print("Diccionario:", datos)

# ---------------------------------------------------------------------------
# clear(): elimina todo el contenido.
# ---------------------------------------------------------------------------

datos.clear()
print("\nDespués de clear:", datos)  # {}

# RESUMEN:
# pop("edad")  -> elimina por clave y devuelve el valor.
# popitem()    -> elimina última pareja y devuelve (clave, valor).
# del d["edad"]-> elimina por clave, no devuelve el valor.
# clear()      -> vacía todo el diccionario.


# =============================================================================
# 11. len(), keys(), values(), items() Y list()
# =============================================================================

datos = {
    "nombre": "Marta",
    "edad": 21,
    "ciudad": "Córdoba"
}

print("\n11. Métodos para consultar:")
print("Número de parejas:", len(datos))  # 3

print("Claves:", datos.keys())
print("Valores:", datos.values())
print("Parejas:", datos.items())

# Si necesito obtener listas:
lista_claves = list(datos.keys())
lista_valores = list(datos.values())
lista_parejas = list(datos.items())

print("Lista de claves:", lista_claves)
print("Lista de valores:", lista_valores)
print("Lista de parejas:", lista_parejas)

# keys(), values() e items() son vistas del diccionario.
# list() las convierte en listas normales.


# =============================================================================
# 12. COPIAR UN DICCIONARIO: copy()
# =============================================================================

original = {
    "nombre": "Ana",
    "edad": 20
}

copia = original.copy()
copia["edad"] = 99

print("\n12. Copiar:")
print("Original:", original)
# {'nombre': 'Ana', 'edad': 20}

print("Copia:", copia)
# {'nombre': 'Ana', 'edad': 99}

# NO CONFUNDIR:
# copia = original
# No crea una copia independiente: las dos variables apuntan al mismo dict.
#
# copia = original.copy()
# Sí crea una copia superficial.


# =============================================================================
# 13. fromkeys(): CREAR CLAVES CON UN MISMO VALOR
# =============================================================================

campos = ["nombre", "edad", "ciudad"]

persona = dict.fromkeys(campos, "Sin rellenar")

print("\n13. fromkeys():")
print(persona)
# {'nombre': 'Sin rellenar', 'edad': 'Sin rellenar',
#  'ciudad': 'Sin rellenar'}

# Si no indicamos valor, se asigna None:
otro = dict.fromkeys(["a", "b"])
print(otro)  # {'a': None, 'b': None}


# =============================================================================
# 14. CREAR UN DICCIONARIO A PARTIR DE DOS LISTAS CON zip()
# =============================================================================

paises = ["España", "Francia", "Italia", "Portugal"]
capitales = ["Madrid", "París", "Roma", "Lisboa"]

# OPCIÓN 1: dict(zip(...)) - forma corta.
diccionario_capitales = dict(zip(paises, capitales))

print("\n14. Diccionario creado con zip():")
print(diccionario_capitales)
# {'España': 'Madrid', 'Francia': 'París',
#  'Italia': 'Roma', 'Portugal': 'Lisboa'}

# OPCIÓN 2: hacerlo manualmente con un for.
diccionario_capitales2 = {}

for pais, capital in zip(paises, capitales):
    diccionario_capitales2[pais] = capital

print(diccionario_capitales2)

# OPCIÓN 3: utilizando índices.
diccionario_capitales3 = {}

for i in range(len(paises)):
    diccionario_capitales3[paises[i]] = capitales[i]

print(diccionario_capitales3)

# ¿QUÉ OPCIÓN ELIJO?
# - Si el ejercicio pide usar zip(): utiliza la opción 1 o 2.
# - Si todavía estás practicando índices: la opción 3 ayuda a entenderlo.
# - Las listas deben estar relacionadas por posición.


# =============================================================================
# 15. DICCIONARIOS CON LISTAS COMO VALORES
# =============================================================================

alumno = {
    "nombre": "Ana",
    "asignaturas": ["Python", "Java", "Bases de datos"]
}

print("\n15. Lista dentro de un diccionario:")
print(alumno["asignaturas"])
# ['Python', 'Java', 'Bases de datos']

# Para acceder a la primera asignatura:
print(alumno["asignaturas"][0])
# Python

# Primero se busca la clave "asignaturas".
# Después se accede al índice 0 de la lista que hemos obtenido.

# Modificar una asignatura:
alumno["asignaturas"][1] = "JavaScript"

# Añadir una asignatura:
alumno["asignaturas"].append("Entornos")

print(alumno)
# La lista interna ha cambiado.


# =============================================================================
# 16. DICCIONARIOS ANIDADOS: UN DICCIONARIO DENTRO DE OTRO
# =============================================================================

alumnos = {
    1: {
        "nombre": "Ana",
        "nota": 8
    },
    2: {
        "nombre": "Luis",
        "nota": 6
    },
    3: {
        "nombre": "Marta",
        "nota": 9
    }
}

# Acceder a un dato:
print("\n16. Diccionarios anidados:")
print(alumnos[1]["nombre"])  # Ana
print(alumnos[2]["nota"])    # 6

# Cómo leer alumnos[1]["nombre"]:
# alumnos[1]          -> obtiene el diccionario del alumno número 1.
# ["nombre"]          -> obtiene el nombre de ese alumno.

# Modificar la nota de Luis:
alumnos[2]["nota"] = 7

# Añadir un alumno:
alumnos[4] = {
    "nombre": "Pedro",
    "nota": 7.5
}

# Recorrer todos los alumnos:
for codigo, datos_alumno in alumnos.items():
    print(
        "Código:", codigo,
        "| Nombre:", datos_alumno["nombre"],
        "| Nota:", datos_alumno["nota"]
    )


# =============================================================================
# 17. EJEMPLO MUY TÍPICO: CONTAR CUÁNTAS VECES APARECE CADA PALABRA
# =============================================================================

palabras = ["sol", "luna", "sol", "mar", "luna", "sol"]

contador = {}

for palabra in palabras:

    # Si la palabra ya está, sumamos 1.
    if palabra in contador:
        contador[palabra] += 1

    # Si no está, la añadimos empezando por 1.
    else:
        contador[palabra] = 1

print("\n17. Contar palabras:")
print(contador)
# {'sol': 3, 'luna': 2, 'mar': 1}

# ESTA ESTRUCTURA ES MUY IMPORTANTE PARA EL EXAMEN:
#
# contador = {}
# for elemento in lista:
#     if elemento in contador:
#         contador[elemento] += 1
#     else:
#         contador[elemento] = 1
#
# ¿Por qué?
# La primera vez que aparece un elemento no existe como clave.
# Las siguientes veces ya existe y aumentamos su contador.


# =============================================================================
# 18. FORMA MÁS CORTA DE CONTAR: get()
# =============================================================================

palabras = ["sol", "luna", "sol", "mar", "luna", "sol"]
contador = {}

for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1

print("\n18. Contar con get():")
print(contador)
# {'sol': 3, 'luna': 2, 'mar': 1}

# EXPLICACIÓN DE ESTA LÍNEA:
# contador.get(palabra, 0)
#     Si la palabra existe, devuelve su contador.
#     Si no existe, devuelve 0.
#
# + 1
#     Sumamos una aparición.
#
# contador[palabra] =
#     Guardamos el resultado en esa clave.


# =============================================================================
# 19. EJEMPLO DE TRADUCCIÓN ESPAÑOL-INGLÉS
# =============================================================================

traducciones = {
    "hola": "hello",
    "casa": "house",
    "perro": "dog",
    "gato": "cat",
    "libro": "book"
}

frase = "hola casa perro".split()
frase_traducida = []

for palabra in frase:

    if palabra in traducciones:
        frase_traducida.append(traducciones[palabra])
    else:
        # Si no existe, dejamos la palabra original.
        frase_traducida.append(palabra)

print("\n19. Traducción:")
print(" ".join(frase_traducida))
# hello house dog

# IDEA:
# 1. Recorro las palabras.
# 2. Compruebo si la palabra está como clave.
# 3. Si existe, uso su valor.
# 4. Si no existe, conservo la palabra original.


# =============================================================================
# 20. EJEMPLO DE AGRUPAR ELEMENTOS EN UN DICCIONARIO
# =============================================================================

# Queremos agrupar nombres por su primera letra.
nombres = ["Ana", "Alberto", "Luis", "Laura", "Marta"]

grupos = {}

for nombre in nombres:
    inicial = nombre[0]

    if inicial not in grupos:
        grupos[inicial] = []

    grupos[inicial].append(nombre)

print("\n20. Agrupar por inicial:")
print(grupos)
# {'A': ['Ana', 'Alberto'], 'L': ['Luis', 'Laura'], 'M': ['Marta']}

# EXPLICACIÓN:
# grupos[inicial] = [] crea una lista vacía para esa letra.
# grupos[inicial].append(nombre) mete el nombre dentro de esa lista.
#
# MUY IMPORTANTE:
# Un diccionario puede guardar listas como valores.


# =============================================================================
# 21. EJEMPLO COMPLETO DE EXAMEN: GESTIÓN DE NOTAS
# =============================================================================

notas = {
    "Ana": 8,
    "Luis": 4,
    "Marta": 9,
    "Pedro": 6
}

print("\n21. Gestión de notas")

# A. Mostrar todos los alumnos y sus notas.
print("TODAS LAS NOTAS:")
for nombre, nota in notas.items():
    print(nombre, ":", nota)

# B. Consultar la nota de un alumno.
alumno_buscar = "Ana"

if alumno_buscar in notas:
    print("La nota de", alumno_buscar, "es", notas[alumno_buscar])
else:
    print("Ese alumno no existe")

# C. Añadir un alumno.
notas["Sonia"] = 7

# D. Modificar una nota.
notas["Luis"] = 5

# E. Eliminar un alumno de forma segura.
alumno_eliminar = "Pedro"

if alumno_eliminar in notas:
    notas.pop(alumno_eliminar)

# F. Mostrar aprobados (nota igual o superior a 5).
print("APROBADOS:")
for nombre, nota in notas.items():
    if nota >= 5:
        print(nombre, nota)

# G. Calcular la media.
suma = 0

for nota in notas.values():
    suma += nota

if len(notas) > 0:
    media = suma / len(notas)
    print("Media:", round(media, 2))
else:
    print("No hay notas")

# H. Encontrar la nota más alta sin utilizar max() sobre el diccionario.
mayor_nota = -1
mejor_alumno = ""

for nombre, nota in notas.items():
    if nota > mayor_nota:
        mayor_nota = nota
        mejor_alumno = nombre

print("Mejor alumno:", mejor_alumno)
print("Nota más alta:", mayor_nota)


# =============================================================================
# 22. OPERACIONES DE CONJUNTOS CON LAS CLAVES DE DOS DICCIONARIOS
# =============================================================================

dic1 = {"a": 1, "b": 2, "c": 3}
dic2 = {"b": 20, "c": 30, "d": 4}

# Claves que están en los dos diccionarios.
print("\n22. Claves comunes:", dic1.keys() & dic2.keys())
# {'b', 'c'}

# Todas las claves, sin repetir.
print("Unión:", dic1.keys() | dic2.keys())
# {'a', 'b', 'c', 'd'} (el orden puede variar)

# Claves que están en dic1 pero no en dic2.
print("Solo dic1:", dic1.keys() - dic2.keys())
# {'a'}

# Claves que están en uno u otro, pero no en ambos.
print("Exclusivas:", dic1.keys() ^ dic2.keys())
# {'a', 'd'}

# También existen los métodos de conjuntos:
# union(), intersection(), difference(), symmetric_difference().
#
# Recuerda: estas operaciones comparan las CLAVES, no sus valores.


# =============================================================================
# 23. ERRORES TÍPICOS Y CÓMO SOLUCIONARLOS
# =============================================================================

"""
ERROR 1: Intentar acceder por posición.
    diccionario[0]
SOLUCIÓN:
    diccionario["nombre"]

ERROR 2: Consultar una clave que no existe.
    print(diccionario["telefono"])
SOLUCIÓN:
    print(diccionario.get("telefono", "No existe"))
    o comprobar antes:
    if "telefono" in diccionario:
        print(diccionario["telefono"])

ERROR 3: Recorrer y pensar que la variable recibe el valor.
    for dato in diccionario:
        print(dato)
REALIDAD:
    dato recibe la CLAVE.
SOLUCIÓN PARA LOS VALORES:
    for dato in diccionario.values():
        print(dato)

ERROR 4: Querer clave y valor sin items().
SOLUCIÓN:
    for clave, valor in diccionario.items():
        print(clave, valor)

ERROR 5: Sumar a una clave que todavía no existe.
    contador[palabra] += 1
PROBLEMA:
    Si la clave no existe, aparece KeyError.
SOLUCIÓN:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
O MÁS CORTO:
    contador[palabra] = contador.get(palabra, 0) + 1

ERROR 6: Confundir añadir y modificar.
    diccionario["edad"] = 20
REALIDAD:
    Si edad no existe, la añade.
    Si edad existe, cambia su valor.

ERROR 7: Pensar que in busca valores.
    "Ana" in diccionario
REALIDAD:
    Comprueba si "Ana" es una CLAVE.
SOLUCIÓN:
    "Ana" in diccionario.values()

ERROR 8: Confundir pop() con popitem().
    pop("nombre") elimina una clave concreta.
    popitem() elimina la última pareja insertada.

ERROR 9: Confundir un diccionario vacío con un conjunto vacío.
    {}     -> diccionario vacío.
    set()  -> conjunto vacío.

ERROR 10: Olvidar que zip() empareja por posición.
    países y capitales deben estar en el mismo orden.
"""


# =============================================================================
# 24. TABLA RÁPIDA: MÉTODOS Y PARA QUÉ SIRVEN
# =============================================================================

"""
OPERACIÓN                         PARA QUÉ SIRVE
---------------------------------------------------------------------------
d = {}                            Crear diccionario vacío.
d = {"a": 1}                      Crear con datos.
dict(parejas)                     Crear desde parejas.
dict(zip(lista1, lista2))         Crear desde dos listas.
dict.fromkeys(claves, valor)      Crear claves con un valor común.
d["a"]                            Consultar el valor de la clave "a".
d.get("a")                        Consultar sin KeyError.
d.get("a", 0)                     Consultar y usar 0 si no existe.
d["a"] = 10                       Añadir o modificar.
d.update(otro)                    Añadir/modificar varias parejas.
d.setdefault("a", 0)              Añadir solo si la clave no existe.
d.pop("a")                        Eliminar clave y devolver su valor.
d.popitem()                       Eliminar última pareja insertada.
del d["a"]                        Eliminar una clave.
d.clear()                         Vaciar el diccionario.
d.copy()                          Crear una copia superficial.
len(d)                            Contar parejas.
d.keys()                          Obtener vista de claves.
d.values()                        Obtener vista de valores.
d.items()                         Obtener vista de parejas.
list(d.keys())                    Convertir claves en lista.
"a" in d                          Comprobar si existe una clave.
10 in d.values()                  Comprobar si existe un valor.
"""

print("\n" + "=" * 78)
print("FIN DE LA CHULETA DE DICCIONARIOS")
print("=" * 78)
