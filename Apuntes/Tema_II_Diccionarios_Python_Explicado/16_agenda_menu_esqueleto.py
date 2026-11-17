# 16 - Esqueleto de agenda con match-case
# Completa cada apartado como ejercicio.

agenda = {}

while True:
    print("\n===== AGENDA =====")
    print("1. Añadir / modificar")
    print("2. Buscar por comienzo del nombre")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion = input("Elige: ")

    match opcion:
        case "1":
            # Pista: nombre in agenda
            # Pista: agenda[nombre] = telefono
            pass

        case "2":
            # Pista: recorre agenda.items()
            # Pista: nombre.startswith(inicio)
            pass

        case "3":
            # Pista: comprueba si existe antes de borrar
            pass

        case "4":
            # Pista: for nombre, telefono in agenda.items()
            pass

        case "5":
            print("Hasta luego")
            break

        case _:
            print("Opción no válida")
