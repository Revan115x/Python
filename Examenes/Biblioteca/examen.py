
libros = {
    10: {
        "Título": "Batman",
        "Autor": "Alan Moore",
        "Año": 1989,
        "Ejemplares": 5
    },

    5: {
        "Título": "El niño de pijama de rayas",
        "Autor": "Juan",
        "Año": 1949,
        "Ejemplares": 1
    }
}

prestamos = {
    "12345678L":{
        "isbn" : 10,
        "Ejemplares" : 1
    }
}


opcion = 0

def Mostrarlibros (libros):
    for isbn, datos in libros.items():
        print("---------------")
        print("ISBN:", isbn)

        for clave, valor in datos.items():
            print(clave, ":", valor)

def AgregarLibro (libros):
    isbn : int = input("CODIGO DE ISBN :") 
    nombre : str = input("NOMBRE DE LIBRO :")
    autor : str = input("NOMBRE DEl AUTOR :")
    ano : int = input("AÑO DE PUBLICACION :")
    ejemplares : int = input("NUMERO DE EJEMPLARES :")

    if isbn in libros:
        print("LIBRO YA EXISTE")
        return False

    libros[isbn] = {
        "Título" : nombre,
        "Autor": autor,
        "Año": ano,
        "Ejemplares": ejemplares
    }

    return True

def AgregarPrestamo (libros,prestamos):
    dni = str(input("NUMERO DE DNI :"))
    isbn = int (input("NUMERO DE ISBN :"))
    ejemplares = int (input("NUMERO DE EJEMPLARES :"))

    if isbn not in libros:
        print("NO EXISTE")

    cantidad = libros[isbn]["Ejemplares"]

    if ejemplares > cantidad:
        print("NO HAY SUFICIENTES EJEMPLARES")
        return False

    total = cantidad - ejemplares

    libros[isbn]["Ejemplares"] = total

    if dni not in prestamos:
        prestamos[dni] = []

    prestamos[dni].append({
        "isbn": isbn,
        "ejemplares": ejemplares
})

def ConsultarPrestamos(prestamos):
    dni = input("NUMERO DE DNI: ")

    if dni not in prestamos:
        print("ESTE USUARIO NO TIENE PRESTAMOS")
        return

    for prestamo in prestamos[dni]:
        print("-------------------")
        print("ISBN:", prestamo["isbn"])
        print("Ejemplares:", prestamo["ejemplares"])


def Estadisticas(libros, prestamos):

    # Número de libros diferentes
    total_libros = len(libros)

    # Contar todos los ejemplares disponibles
    total_ejemplares = 0

    for isbn, datos in libros.items():
        total_ejemplares += datos["Ejemplares"]

    # Contar préstamos y ejemplares prestados
    total_prestamos = 0
    ejemplares_prestados = 0

    for dni, lista in prestamos.items():
        for prestamo in lista:
            total_prestamos += 1
            ejemplares_prestados += prestamo["ejemplares"]

    print("===== ESTADISTICAS =====")
    
def menu():
    while True:
        print("\n===== Biblioteca =====")
        print("1. Mostrar todos los libros")
        print("2. Registrar un nuevo libro")
        print("3. Realizar un préstamo")
        print("4. Consultar préstamos de un socio")
        print("5. Estadísticas")
        print("0. Salir")
        opcion = int(input("Elige una opción: "))
        
        match opcion:
            case 1:
                print("Lista de libros")
                Mostrarlibros(libros)
            case 2:
                if AgregarLibro(libros) == True:
                    print("LIBRO AGREGADO")
                else:
                    print("ERROR")
            case 3:
                AgregarPrestamo(libros,prestamos)
            case 4:
                ConsultarPrestamos(prestamos)
            case 0:
                break

menu()