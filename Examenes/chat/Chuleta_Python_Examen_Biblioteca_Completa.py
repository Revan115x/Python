"""
CHULETA DE EXAMEN PYTHON - BIBLIOTECA DAW
=========================================

Esta chuleta está construida SOBRE EL EXAMEN DE LA BIBLIOTECA.
No es una chuleta general: todos los ejemplos utilizan libros, socios,
préstamos, ISBN, ejemplares y estadísticas.

Úsala para consultar CÓMO se hace cada operación y adaptar el ejemplo
al enunciado que te pongan.

CONDICIONES:
- Nivel inicial de DAW.
- Un único archivo .py.
- Sin import.
- Sin try / except / raise.
- Ejemplos independientes: algunos vuelven a crear las variables.
- Los resultados aparecen en comentarios.
- No ejecutes todo el archivo de golpe: contiene ejemplos de consulta.

ÍNDICE
------
1. Crear libros de distintas maneras
2. Crear datos desde listas y usar zip()
3. Acceder a los datos de un libro
4. Mostrar libros de todas las maneras habituales
5. Añadir libros
6. Modificar libros
7. Eliminar libros
8. Buscar y filtrar libros
9. Listas relacionadas con libros
10. Préstamos: estructuras posibles
11. Añadir, consultar y recorrer préstamos
12. Devolver libros
13. Unir y comparar listas / conjuntos
14. Estadísticas típicas del examen
15. Funciones: patrones para cada apartado
16. Menú while + match-case
17. Validaciones sin excepciones
18. Errores típicos del examen
19. Plantillas rápidas para adaptar
"""


# ============================================================
# 1. CREAR LOS LIBROS DE DISTINTAS MANERAS
# ============================================================

# FORMA A: diccionario con ISBN como clave y otro diccionario dentro.
# Es la estructura que usamos en el examen de biblioteca.

libros = {
    10: {
        "Titulo": "Batman",
        "Autor": "Alan Moore",
        "Anio": 1989,
        "Ejemplares": 5
    },
    5: {
        "Titulo": "El niño de pijama de rayas",
        "Autor": "Juan",
        "Anio": 1949,
        "Ejemplares": 1
    },
    8: {
        "Titulo": "Spider-Man Blue",
        "Autor": "Jeph Loeb",
        "Anio": 2002,
        "Ejemplares": 3
    }
}

# FORMA B: crear primero un diccionario vacío y añadir libros después.
libros_vacios = {}

libros_vacios[10] = {
    "Titulo": "Batman",
    "Autor": "Alan Moore",
    "Anio": 1989,
    "Ejemplares": 5
}

libros_vacios[5] = {
    "Titulo": "Zelda",
    "Autor": "Nintendo",
    "Anio": 2017,
    "Ejemplares": 4
}

# FORMA C: guardar libros en una LISTA DE DICCIONARIOS.
# Aquí el ISBN también está dentro de cada libro.
libros_lista = [
    {"ISBN": 10, "Titulo": "Batman", "Autor": "Alan Moore", "Ejemplares": 5},
    {"ISBN": 5, "Titulo": "Zelda", "Autor": "Nintendo", "Ejemplares": 4}
]

# DIFERENCIA:
# libros[10]              -> busca por la clave ISBN 10.
# libros_lista[0]         -> busca por posición 0.
# libros_lista[0]["Titulo"] -> título del primer libro.


# ============================================================
# 2. CREAR DATOS DESDE LISTAS Y USAR zip()
# ============================================================

# CASO 1: juntar dos listas elemento a elemento con zip().
isbn_lista = [10, 5, 8]
titulos = ["Batman", "Zelda", "Spider-Man Blue"]

parejas = list(zip(isbn_lista, titulos))
print(parejas)
# Resultado: [(10, 'Batman'), (5, 'Zelda'), (8, 'Spider-Man Blue')]

# zip() empareja el primer elemento de cada lista,
# después el segundo, después el tercero...

# CASO 2: crear un diccionario sencillo con dos listas.
isbn_lista = [10, 5, 8]
titulos = ["Batman", "Zelda", "Spider-Man Blue"]

isbn_titulo = dict(zip(isbn_lista, titulos))
print(isbn_titulo)
# Resultado: {10: 'Batman', 5: 'Zelda', 8: 'Spider-Man Blue'}

# CASO 3: crear un diccionario de libros usando varias listas.
isbn_lista = [10, 5, 8]
titulos = ["Batman", "Zelda", "Spider-Man Blue"]
autores = ["Alan Moore", "Nintendo", "Jeph Loeb"]
ejemplares = [5, 4, 3]

libros_desde_listas = {}

for isbn, titulo, autor, cantidad in zip(
    isbn_lista, titulos, autores, ejemplares
):
    libros_desde_listas[isbn] = {
        "Titulo": titulo,
        "Autor": autor,
        "Ejemplares": cantidad
    }

print(libros_desde_listas)
# Resultado: cada ISBN queda asociado a su diccionario de datos.

# CASO 4: crear un diccionario usando dict(zip()) de dos listas.
campos = ["Titulo", "Autor", "Ejemplares"]
datos = ["Batman", "Alan Moore", 5]

libro = dict(zip(campos, datos))
print(libro)
# Resultado: {'Titulo': 'Batman', 'Autor': 'Alan Moore', 'Ejemplares': 5}

# CASO 5: juntar listas con +.
titulos_a = ["Batman", "Zelda"]
titulos_b = ["Mario", "Pokemon"]

todos_titulos = titulos_a + titulos_b
print(todos_titulos)
# Resultado: ['Batman', 'Zelda', 'Mario', 'Pokemon']

# OJO:
# + junta listas completas.
# zip() empareja elementos que están en la misma posición.

# CASO 6: añadir una lista a otra.
titulos_a.extend(titulos_b)
print(titulos_a)
# Resultado: ['Batman', 'Zelda', 'Mario', 'Pokemon']

# Diferencia:
# lista.append(otra_lista) -> añade la lista como un solo elemento.
# lista.extend(otra_lista) -> añade cada elemento por separado.


# ============================================================
# 3. ACCEDER A LOS DATOS DE UN LIBRO
# ============================================================

libros = {
    10: {"Titulo": "Batman", "Autor": "Alan Moore", "Anio": 1989, "Ejemplares": 5},
    5: {"Titulo": "Zelda", "Autor": "Nintendo", "Anio": 2017, "Ejemplares": 4}
}

# Acceder al libro completo:
print(libros[10])
# Resultado: {'Titulo': 'Batman', 'Autor': 'Alan Moore', ...}

# Acceder a un campo:
print(libros[10]["Titulo"])
# Resultado: Batman

print(libros[10]["Ejemplares"])
# Resultado: 5

# Guardar el dato en una variable:
titulo = libros[10]["Titulo"]
stock = libros[10]["Ejemplares"]

# Acceder con get() al ISBN:
datos_libro = libros.get(10)
print(datos_libro)

# get() para una clave interior:
print(libros[10].get("Autor"))
# Resultado: Alan Moore

# Comprobar antes de acceder:
isbn = 10

if isbn in libros:
    print(libros[isbn]["Titulo"])
else:
    print("Libro no encontrado")

# IMPORTANTE:
# "Ejemplares" y "ejemplares" son claves distintas.
# Respeta mayúsculas y minúsculas tal como las creaste.


# ============================================================
# 4. MOSTRAR LIBROS DE TODAS LAS MANERAS HABITUALES
# ============================================================

libros = {
    10: {"Titulo": "Batman", "Autor": "Alan Moore", "Anio": 1989, "Ejemplares": 5},
    5: {"Titulo": "Zelda", "Autor": "Nintendo", "Anio": 2017, "Ejemplares": 4}
}

# FORMA A: mostrar el diccionario completo.
print(libros)

# FORMA B: recorrer ISBN y datos.
for isbn, datos in libros.items():
    print("ISBN:", isbn)
    print("Titulo:", datos["Titulo"])
    print("Autor:", datos["Autor"])
    print("Año:", datos["Anio"])
    print("Ejemplares:", datos["Ejemplares"])
    print("------------------")

# FORMA C: recorrer todos los campos interiores.
for isbn, datos in libros.items():
    print("LIBRO:", isbn)
    for clave, valor in datos.items():
        print(clave, ":", valor)

# FORMA D: mostrar solo títulos.
for isbn, datos in libros.items():
    print(datos["Titulo"])

# FORMA E: mostrar ISBN y título.
for isbn, datos in libros.items():
    print(isbn, "-", datos["Titulo"])

# FORMA F: mostrar solo libros con ejemplares disponibles.
for isbn, datos in libros.items():
    if datos["Ejemplares"] > 0:
        print(datos["Titulo"], "disponible")

# FORMA G: mostrar libros agotados.
for isbn, datos in libros.items():
    if datos["Ejemplares"] == 0:
        print(datos["Titulo"], "AGOTADO")


# ============================================================
# 5. AÑADIR LIBROS
# ============================================================

libros = {
    10: {"Titulo": "Batman", "Autor": "Alan Moore", "Anio": 1989, "Ejemplares": 5}
}

# FORMA A: añadir directamente.
libros[5] = {
    "Titulo": "Zelda",
    "Autor": "Nintendo",
    "Anio": 2017,
    "Ejemplares": 4
}

# FORMA B: añadir con variables.
isbn = 8
titulo = "Spider-Man Blue"
autor = "Jeph Loeb"
anio = 2002
cantidad = 3

if isbn not in libros:
    libros[isbn] = {
        "Titulo": titulo,
        "Autor": autor,
        "Anio": anio,
        "Ejemplares": cantidad
    }
    print("Libro añadido")
else:
    print("El ISBN ya existe")

# FORMA C: añadir datos a un diccionario vacío.
nuevo_libro = {}
nuevo_libro["Titulo"] = "Mario"
nuevo_libro["Autor"] = "Nintendo"
nuevo_libro["Anio"] = 2023
nuevo_libro["Ejemplares"] = 6

libros[20] = nuevo_libro

# RECUERDA:
# libros[isbn] = {...} añade o sustituye el libro con ese ISBN.
# Si no quieres sobrescribir, comprueba antes: if isbn not in libros.


# ============================================================
# 6. MODIFICAR LIBROS
# ============================================================

libros = {
    10: {"Titulo": "Batman", "Autor": "Alan Moore", "Anio": 1989, "Ejemplares": 5},
    5: {"Titulo": "Zelda", "Autor": "Nintendo", "Anio": 2017, "Ejemplares": 4}
}

# MODIFICAR un campo concreto.
libros[10]["Ejemplares"] = 12

# Modificar el título.
libros[10]["Titulo"] = "Batman: Año Uno"

# Modificar varios campos.
if 5 in libros:
    libros[5]["Autor"] = "Nintendo EPD"
    libros[5]["Ejemplares"] = 10

# AUMENTAR ejemplares existentes.
libros[10]["Ejemplares"] += 3

# RESTAR ejemplares existentes.
libros[10]["Ejemplares"] -= 2

# Pedir ISBN y modificar stock.
isbn = 10
nueva_cantidad = 15

if isbn in libros:
    libros[isbn]["Ejemplares"] = nueva_cantidad
    print("Stock actualizado")
else:
    print("Libro no encontrado")


# ============================================================
# 7. ELIMINAR LIBROS
# ============================================================

libros = {
    10: {"Titulo": "Batman", "Ejemplares": 5},
    5: {"Titulo": "Zelda", "Ejemplares": 4}
}

# FORMA A: eliminar por clave con del.
del libros[10]

# FORMA B: eliminar con pop().
eliminado = libros.pop(5)
print(eliminado)
# Devuelve el diccionario interior del libro eliminado.

# FORMA C: comprobar antes de eliminar.
isbn = 10

if isbn in libros:
    libros.pop(isbn)
    print("Libro eliminado")
else:
    print("No existe")

# Vaciar todos los libros:
# libros.clear()


# ============================================================
# 8. BUSCAR Y FILTRAR LIBROS
# ============================================================

libros = {
    10: {"Titulo": "Batman", "Autor": "Alan Moore", "Anio": 1989, "Ejemplares": 5},
    5: {"Titulo": "Zelda", "Autor": "Nintendo", "Anio": 2017, "Ejemplares": 0},
    8: {"Titulo": "Spider-Man Blue", "Autor": "Jeph Loeb", "Anio": 2002, "Ejemplares": 3}
}

# BUSCAR por ISBN.
isbn = 10
if isbn in libros:
    print(libros[isbn])
else:
    print("No existe")

# BUSCAR por título recorriendo los libros.
titulo_buscar = "Zelda"
encontrado = False

for isbn, datos in libros.items():
    if datos["Titulo"] == titulo_buscar:
        print("ISBN:", isbn)
        print("Autor:", datos["Autor"])
        encontrado = True

if encontrado == False:
    print("Título no encontrado")

# BUSCAR por autor.
autor_buscar = "Alan Moore"

for isbn, datos in libros.items():
    if datos["Autor"] == autor_buscar:
        print(datos["Titulo"])

# FILTRAR libros publicados después del año 2000.
for isbn, datos in libros.items():
    if datos["Anio"] > 2000:
        print(datos["Titulo"])

# FILTRAR libros que tienen al menos 3 ejemplares.
for isbn, datos in libros.items():
    if datos["Ejemplares"] >= 3:
        print(datos["Titulo"], datos["Ejemplares"])

# BUSCAR el libro con más ejemplares.
mayor_stock = -1
isbn_mayor = None

for isbn, datos in libros.items():
    if datos["Ejemplares"] > mayor_stock:
        mayor_stock = datos["Ejemplares"]
        isbn_mayor = isbn

if isbn_mayor is not None:
    print("Más ejemplares:", libros[isbn_mayor]["Titulo"])
    print("Cantidad:", mayor_stock)


# ============================================================
# 9. LISTAS RELACIONADAS CON LIBROS
# ============================================================

# Crear una lista vacía de títulos.
titulos = []

# Recoger títulos del diccionario.
for isbn, datos in libros.items():
    titulos.append(datos["Titulo"])

print(titulos)

# Crear una lista con los ISBN.
lista_isbn = []

for isbn in libros:
    lista_isbn.append(isbn)

print(lista_isbn)

# Crear una lista con autores.
autores = []

for isbn, datos in libros.items():
    autores.append(datos["Autor"])

# Quitar autores repetidos convirtiendo la lista en set.
autores_unicos = set(autores)
print(autores_unicos)

# Contar libros de un autor.
contador = 0
for isbn, datos in libros.items():
    if datos["Autor"] == "Alan Moore":
        contador += 1

print("Libros de Alan Moore:", contador)

# Copiar una lista de títulos.
copia_titulos = titulos.copy()

# Ordenar títulos alfabéticamente.
titulos.sort()

# Ordenar títulos alfabéticamente sin modificar la lista original.
titulos_ordenados = sorted(titulos)


# ============================================================
# 10. PRÉSTAMOS: ESTRUCTURAS POSIBLES
# ============================================================

# ESTRUCTURA RECOMENDADA PARA EL EXAMEN:
# Un DNI puede tener VARIOS préstamos.
# Por eso cada DNI guarda una LISTA de diccionarios.

prestamos = {
    "12345678L": [
        {"isbn": 10, "ejemplares": 1},
        {"isbn": 5, "ejemplares": 2}
    ],
    "87654321A": [
        {"isbn": 8, "ejemplares": 1}
    ]
}

# Cómo se interpreta:
# prestamos["12345678L"] -> lista de préstamos de ese socio.
# prestamos["12345678L"][0] -> primer préstamo.
# prestamos["12345678L"][0]["isbn"] -> ISBN del primer préstamo.

# OTRA ESTRUCTURA POSIBLE:
# Una lista de diccionarios. Cada préstamo es un registro.
prestamos_lista = [
    {"dni": "12345678L", "isbn": 10, "ejemplares": 1},
    {"dni": "12345678L", "isbn": 5, "ejemplares": 2},
    {"dni": "87654321A", "isbn": 8, "ejemplares": 1}
]

# Diferencia:
# Diccionario de listas: cómodo para consultar por DNI.
# Lista de diccionarios: cómodo para recorrer todos los préstamos.


# ============================================================
# 11. AÑADIR, CONSULTAR Y RECORRER PRÉSTAMOS
# ============================================================

prestamos = {}

# AÑADIR un préstamo si el socio todavía no existe.
dni = "12345678L"
isbn = 10
cantidad = 2

if dni not in prestamos:
    prestamos[dni] = []

prestamos[dni].append({
    "isbn": isbn,
    "ejemplares": cantidad
})

# AÑADIR otro préstamo al mismo socio.
prestamos[dni].append({
    "isbn": 5,
    "ejemplares": 1
})

# CONSULTAR si un socio tiene préstamos.
if dni in prestamos:
    print("Tiene préstamos")
else:
    print("No tiene préstamos")

# MOSTRAR los préstamos de un socio.
if dni in prestamos:
    for prestamo in prestamos[dni]:
        print("ISBN:", prestamo["isbn"])
        print("Ejemplares:", prestamo["ejemplares"])
else:
    print("Socio sin préstamos")

# MOSTRAR todos los préstamos de todos los socios.
for dni, lista in prestamos.items():
    print("SOCIO:", dni)

    for prestamo in lista:
        print("ISBN:", prestamo["isbn"])
        print("Ejemplares:", prestamo["ejemplares"])

# CONTAR préstamos de un socio.
if dni in prestamos:
    print("Préstamos del socio:", len(prestamos[dni]))

# CONTAR todos los préstamos.
total_prestamos = 0

for dni, lista in prestamos.items():
    total_prestamos += len(lista)

print("Todos los préstamos:", total_prestamos)

# SUMAR ejemplares prestados.
total_ejemplares_prestados = 0

for dni, lista in prestamos.items():
    for prestamo in lista:
        total_ejemplares_prestados += prestamo["ejemplares"]

print("Ejemplares prestados:", total_ejemplares_prestados)

# BUSCAR si un socio tiene prestado un ISBN concreto.
dni = "12345678L"
isbn_buscar = 10
encontrado = False

if dni in prestamos:
    for prestamo in prestamos[dni]:
        if prestamo["isbn"] == isbn_buscar:
            print("El socio tiene este libro prestado")
            encontrado = True

if encontrado == False:
    print("No tiene ese préstamo")


# ============================================================
# 12. DEVOLVER LIBROS
# ============================================================

# EJEMPLO: devolver un préstamo completo.
libros = {
    10: {"Titulo": "Batman", "Ejemplares": 3}
}

prestamos = {
    "12345678L": [
        {"isbn": 10, "ejemplares": 2},
        {"isbn": 5, "ejemplares": 1}
    ]
}

dni = "12345678L"
isbn_devolver = 10

if dni in prestamos:
    encontrado = False

    for prestamo in prestamos[dni]:
        if prestamo["isbn"] == isbn_devolver:
            cantidad_devuelta = prestamo["ejemplares"]

            # Devolver ejemplares al inventario.
            libros[isbn_devolver]["Ejemplares"] += cantidad_devuelta

            # Eliminar ese préstamo de la lista.
            prestamos[dni].remove(prestamo)

            encontrado = True
            print("Devolución realizada")
            break

    if encontrado == False:
        print("El socio no tiene ese libro prestado")
else:
    print("Socio sin préstamos")

# IMPORTANTE:
# Si eliminas elementos de una lista mientras la recorres,
# utiliza break justo después de remove() para salir del bucle.


# ============================================================
# 13. UNIR Y COMPARAR LISTAS / CONJUNTOS
# ============================================================

# Dos listas de libros leídos por dos socios.
socio_a = ["Batman", "Zelda", "Mario"]
socio_b = ["Zelda", "Pokemon", "Mario"]

# UNIR las listas: mantiene también los repetidos.
todos = socio_a + socio_b
print(todos)
# Resultado: ['Batman', 'Zelda', 'Mario', 'Zelda', 'Pokemon', 'Mario']

# UNIR sin repetidos usando set.
todos_sin_repetir = set(socio_a) | set(socio_b)
print(todos_sin_repetir)
# El orden de un set puede variar.

# ELEMENTOS COMUNES: aparecen en ambos grupos.
comunes = set(socio_a) & set(socio_b)
print(comunes)
# Contiene Zelda y Mario.

# SOLO los del socio A.
solo_a = set(socio_a) - set(socio_b)
print(solo_a)
# Contiene Batman.

# SOLO los del socio B.
solo_b = set(socio_b) - set(socio_a)
print(solo_b)
# Contiene Pokemon.

# MISMAS operaciones usando métodos:
union = set(socio_a).union(set(socio_b))
interseccion = set(socio_a).intersection(set(socio_b))
diferencia = set(socio_a).difference(set(socio_b))

# Eliminar repetidos de una lista:
autores = ["Alan Moore", "Juan", "Alan Moore"]
autores_sin_repetir = list(set(autores))


# ============================================================
# 14. ESTADÍSTICAS TÍPICAS DEL EXAMEN
# ============================================================

libros = {
    10: {"Titulo": "Batman", "Ejemplares": 5},
    5: {"Titulo": "Zelda", "Ejemplares": 0},
    8: {"Titulo": "Spider-Man Blue", "Ejemplares": 3}
}

prestamos = {
    "12345678L": [
        {"isbn": 10, "ejemplares": 2},
        {"isbn": 5, "ejemplares": 1}
    ],
    "87654321A": [
        {"isbn": 8, "ejemplares": 1}
    ]
}

# 1. Número de libros diferentes.
total_libros = len(libros)
print("Libros diferentes:", total_libros)
# Resultado: 3

# 2. Número total de ejemplares disponibles.
total_disponibles = 0

for isbn, datos in libros.items():
    total_disponibles += datos["Ejemplares"]

print("Disponibles:", total_disponibles)
# Resultado: 8

# 3. Número total de préstamos.
total_prestamos = 0

for dni, lista in prestamos.items():
    total_prestamos += len(lista)

print("Préstamos:", total_prestamos)
# Resultado: 3

# 4. Número total de ejemplares prestados.
total_prestados = 0

for dni, lista in prestamos.items():
    for prestamo in lista:
        total_prestados += prestamo["ejemplares"]

print("Ejemplares prestados:", total_prestados)
# Resultado: 4

# 5. Número de socios con préstamos.
total_socios = len(prestamos)
print("Socios con préstamos:", total_socios)
# Resultado: 2

# 6. Libro con más ejemplares disponibles.
mayor = -1
titulo_mayor = ""

for isbn, datos in libros.items():
    if datos["Ejemplares"] > mayor:
        mayor = datos["Ejemplares"]
        titulo_mayor = datos["Titulo"]

print("Mayor stock:", titulo_mayor, mayor)

# 7. Libro con menos ejemplares disponibles.
menor = None
titulo_menor = ""

for isbn, datos in libros.items():
    if menor is None or datos["Ejemplares"] < menor:
        menor = datos["Ejemplares"]
        titulo_menor = datos["Titulo"]

print("Menor stock:", titulo_menor, menor)

# 8. Contar libros agotados.
agotados = 0

for isbn, datos in libros.items():
    if datos["Ejemplares"] == 0:
        agotados += 1

print("Libros agotados:", agotados)

# 9. Media de ejemplares por libro.
if len(libros) > 0:
    media = total_disponibles / len(libros)
    print("Media de ejemplares:", media)


# ============================================================
# 15. FUNCIONES: PATRONES PARA CADA APARTADO
# ============================================================

# FUNCIÓN PARA MOSTRAR:
def mostrar_libros(libros):
    for isbn, datos in libros.items():
        print(isbn, datos["Titulo"], datos["Ejemplares"])

# FUNCIÓN PARA AÑADIR:
def anadir_libro(libros, isbn, titulo, autor, anio, ejemplares):
    if isbn in libros:
        return False

    libros[isbn] = {
        "Titulo": titulo,
        "Autor": autor,
        "Anio": anio,
        "Ejemplares": ejemplares
    }
    return True

# FUNCIÓN PARA MODIFICAR:
def modificar_stock(libros, isbn, cantidad):
    if isbn not in libros:
        return False

    libros[isbn]["Ejemplares"] = cantidad
    return True

# FUNCIÓN PARA BUSCAR Y DEVOLVER:
def buscar_libro(libros, isbn):
    if isbn in libros:
        return libros[isbn]

    return None

# FUNCIÓN PARA CALCULAR Y DEVOLVER UN TOTAL:
def contar_ejemplares(libros):
    total = 0

    for isbn, datos in libros.items():
        total += datos["Ejemplares"]

    return total

# FUNCIÓN QUE RECIBE VARIAS ESTRUCTURAS:
def hacer_prestamo(libros, prestamos, dni, isbn, cantidad):
    if isbn not in libros:
        print("El libro no existe")
        return False

    if cantidad <= 0:
        print("Cantidad incorrecta")
        return False

    if cantidad > libros[isbn]["Ejemplares"]:
        print("No hay ejemplares suficientes")
        return False

    libros[isbn]["Ejemplares"] -= cantidad

    if dni not in prestamos:
        prestamos[dni] = []

    prestamos[dni].append({
        "isbn": isbn,
        "ejemplares": cantidad
    })

    return True

# EJEMPLO DE CÓMO LLAMAR A UNA FUNCIÓN:
# anadir_libro(libros, 20, "Mario", "Nintendo", 2023, 4)
# resultado = buscar_libro(libros, 10)
# total = contar_ejemplares(libros)


# ============================================================
# 16. MENÚ WHILE + MATCH-CASE
# ============================================================

def menu():
    while True:
        print("\\n===== BIBLIOTECA =====")
        print("1. Mostrar libros")
        print("2. Añadir libro")
        print("3. Modificar stock")
        print("4. Buscar libro")
        print("5. Estadísticas")
        print("0. Salir")

        # Si input() se deja así, opcion es str.
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                print("Mostrar libros")

            case "2":
                print("Añadir libro")

            case "3":
                print("Modificar stock")

            case "4":
                print("Buscar libro")

            case "5":
                print("Estadísticas")

            case "0":
                print("Hasta luego")
                break

            case _:
                print("Opción incorrecta")

# IMPORTANTE:
# Si haces opcion = int(input(...)), usa case 1:, case 2: ...
# Si haces opcion = input(...), usa case "1":, case "2": ...


# ============================================================
# 17. VALIDACIONES SIN EXCEPCIONES
# ============================================================

# Comprobar que un texto no está vacío.
titulo = " Batman "

if titulo.strip() == "":
    print("El título está vacío")

# strip() elimina espacios al principio y al final.
titulo = titulo.strip()
print(titulo)
# Resultado: Batman

# Comprobar si un texto contiene solo números.
texto = "123"

if texto.isdigit():
    numero = int(texto)
    print("Número:", numero)
else:
    print("Introduce números")

# Comprobar ISBN si el ejercicio lo trata como número.
isbn = 10
if isbn <= 0:
    print("ISBN incorrecto")

# Comprobar que el año sea razonable.
anio = 2026
if anio <= 0 or anio > 2026:
    print("Año no válido")

# Comprobar cantidad positiva.
cantidad = 2
if cantidad <= 0:
    print("La cantidad debe ser mayor que cero")

# Comprobar que un dato pertenece a una lista permitida.
tipo = "Lectura"
tipos = ["Lectura", "Consulta", "Referencia"]

if tipo in tipos:
    print("Tipo válido")
else:
    print("Tipo no válido")


# ============================================================
# 18. ERRORES TÍPICOS DEL EXAMEN
# ============================================================

# ERROR 1: input() devuelve texto.
# MAL:
# isbn: int = input("ISBN: ")
# BIEN:
# isbn = int(input("ISBN: "))


# ERROR 2: comprobar una clave.
# MAL:
# if isbn in "ISBN":
# BIEN:
# if isbn in libros:


# ERROR 3: mayúsculas y minúsculas.
# Si creaste "Ejemplares", accede con:
# libros[isbn]["Ejemplares"]
# No con:
# libros[isbn]["ejemplares"]


# ERROR 4: reemplazar todo el diccionario.
# MAL:
# libros = {"Titulo": titulo}
# BIEN:
# libros[isbn] = {"Titulo": titulo}


# ERROR 5: continuar cuando el ISBN no existe.
# MAL:
# if isbn not in libros:
#     print("No existe")
#     # El programa sigue y libros[isbn] puede fallar.
# BIEN:
# if isbn not in libros:
#     print("No existe")
#     return False


# ERROR 6: append() no es para diccionarios.
# Para añadir una clave:
# libros[isbn] = datos
# Para añadir a una lista:
# prestamos[dni].append(prestamo)


# ERROR 7: si un socio puede tener varios préstamos,
# no guardes un único diccionario directamente en prestamos[dni].
# Guarda una lista:
# if dni not in prestamos:
#     prestamos[dni] = []
# prestamos[dni].append(nuevo_prestamo)


# ERROR 8: no mezcles int y str al comparar claves.
# 10 != "10"
# Convierte el input si las claves son números.


# ERROR 9: no uses range(len(diccionario)) para recorrer
# las claves y valores de un diccionario.
# Utiliza:
# for clave, valor in diccionario.items():


# ERROR 10: = asigna; == compara.
# isbn = 10
# if isbn == 10:
#     print("Es el ISBN 10")


# ERROR 11: no sumes un diccionario directamente.
# Para sumar el campo Ejemplares:
# total = 0
# for isbn, datos in libros.items():
#     total += datos["Ejemplares"]


# ERROR 12: len(prestamos) cuenta los DNI/socios,
# no todos los préstamos si cada socio tiene una lista.
# Para contar todos los préstamos:
# total = 0
# for dni, lista in prestamos.items():
#     total += len(lista)


# ============================================================
# 19. PLANTILLAS RÁPIDAS PARA COPIAR Y ADAPTAR
# ============================================================

# A) MOSTRAR UN DICCIONARIO ANIDADO:
#
# for codigo, datos in diccionario.items():
#     print("Código:", codigo)
#     for campo, valor in datos.items():
#         print(campo, ":", valor)


# B) AÑADIR UN REGISTRO A UN DICCIONARIO:
#
# diccionario[codigo] = {
#     "nombre": nombre,
#     "cantidad": cantidad
# }


# C) MODIFICAR UN CAMPO:
#
# if codigo in diccionario:
#     diccionario[codigo]["cantidad"] = nueva_cantidad


# D) ELIMINAR UNA CLAVE:
#
# if codigo in diccionario:
#     diccionario.pop(codigo)


# E) AÑADIR A UNA LISTA DENTRO DE UN DICCIONARIO:
#
# if dni not in prestamos:
#     prestamos[dni] = []
#
# prestamos[dni].append({
#     "isbn": isbn,
#     "ejemplares": cantidad
# })


# F) RECORRER LOS PRÉSTAMOS DE UN SOCIO:
#
# if dni in prestamos:
#     for prestamo in prestamos[dni]:
#         print(prestamo["isbn"])
#         print(prestamo["ejemplares"])


# G) RECORRER TODOS LOS PRÉSTAMOS:
#
# for dni, lista in prestamos.items():
#     for prestamo in lista:
#         print(dni, prestamo["isbn"], prestamo["ejemplares"])


# H) SUMAR TODOS LOS EJEMPLARES DISPONIBLES:
#
# total = 0
# for isbn, datos in libros.items():
#     total += datos["Ejemplares"]


# I) CONTAR TODOS LOS PRÉSTAMOS:
#
# total = 0
# for dni, lista in prestamos.items():
#     total += len(lista)


# J) BUSCAR POR UN CAMPO QUE NO ES LA CLAVE:
#
# encontrado = False
# for isbn, datos in libros.items():
#     if datos["Titulo"] == titulo_buscar:
#         print(isbn, datos)
#         encontrado = True
#
# if encontrado == False:
#     print("No encontrado")


# K) ZIP PARA CREAR UN DICCIONARIO:
#
# codigos = [10, 20, 30]
# nombres = ["Batman", "Zelda", "Mario"]
# diccionario = dict(zip(codigos, nombres))


# L) UNIR DOS LISTAS:
#
# lista_final = lista_a + lista_b
#
# O añadir los elementos de una lista a otra:
# lista_a.extend(lista_b)


# M) QUITAR REPETIDOS:
#
# lista_sin_repetidos = list(set(lista))


# N) UNIÓN / INTERSECCIÓN / DIFERENCIA:
#
# union = set(lista_a) | set(lista_b)
# comunes = set(lista_a) & set(lista_b)
# solo_a = set(lista_a) - set(lista_b)
#
# También:
# union = set(lista_a).union(set(lista_b))
# comunes = set(lista_a).intersection(set(lista_b))
# solo_a = set(lista_a).difference(set(lista_b))


# FIN DE LA CHULETA
#
# PREGUNTA CLAVE ANTES DE PROGRAMAR:
# 1. ¿Tengo una colección de valores? -> lista.
# 2. ¿Tengo datos identificados por una clave? -> diccionario.
# 3. ¿Cada clave tiene varios registros? -> diccionario de listas.
# 4. ¿Cada registro tiene varios campos? -> diccionario dentro de diccionario
#    o lista de diccionarios.
# 5. ¿Necesito emparejar datos de varias listas? -> zip().
# 6. ¿Necesito eliminar repetidos o comparar grupos? -> set().
