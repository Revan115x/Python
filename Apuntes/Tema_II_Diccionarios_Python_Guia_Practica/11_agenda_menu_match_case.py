# AGENDA CON MENU: CONSULTAR, AÑADIR, MODIFICAR Y ELIMINAR
# Requiere Python 3.10 o superior por match-case.
agenda = {}

while True:
    print("\n1 Mostrar | 2 Buscar | 3 Añadir | 4 Modificar | 5 Eliminar | 0 Salir")
    opcion = input("Opción: ")

    match opcion:
        case "1":
            for nombre, telefono in agenda.items():
                print(nombre, telefono)
            if len(agenda) == 0:
                print("AGENDA VACÍA")

        case "2":
            nombre = input("Nombre: ")
            if nombre in agenda:
                print("NOMBRE:", nombre)
                print("TELÉFONO:", agenda[nombre])
            else:
                print("NO ENCONTRADO")

        case "3":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            agenda[nombre] = telefono
            print("GUARDADO")

        case "4":
            nombre = input("Nombre: ")
            if nombre in agenda:
                agenda[nombre] = input("Nuevo teléfono: ")
                print("MODIFICADO")
            else:
                print("NO ENCONTRADO")

        case "5":
            nombre = input("Nombre: ")
            if nombre in agenda:
                del agenda[nombre]
                print("ELIMINADO")
            else:
                print("NO ENCONTRADO")

        case "0":
            print("SALIENDO")
            break

        case _:
            print("OPCIÓN NO VÁLIDA")
