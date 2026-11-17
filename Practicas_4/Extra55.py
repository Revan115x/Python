
alumnos = {
    "A001": {
        "nombre": "Carlos",
        "edad": 20,
        "nota": 7.5
    },
    "A002": {
        "nombre": "Lucia",
        "edad": 21,
        "nota": 8.0
    },
    "A003": {
        "nombre": "Pedro",
        "edad": 19,
        "nota": 4.5
    }
}

opcion = 0

while opcion != 9:

    print("\n====== MENU ALUMNOS ======")
    print("1. Mostrar todos los alumnos")
    print("2. Buscar un alumno")
    print("3. Añadir un alumno")
    print("4. Modificar nota")
    print("5. Eliminar alumno")
    print("6. Calcular media")
    print("7. Mostrar alumnos con nota superior a 5")
    print("8. Contar alumnos")
    print("9. Salir")

    opcion = int(input("Selecciona una opcion: "))

    match opcion:

        # 1. Mostrar todos los alumnos
        case 1:
            for clave, valor in alumnos.items():
                print(clave, valor)

        # 2. Buscar un alumno
        case 2:
            cod = input("DIME EL CODIGO DEL ALUMNO: ")

            if cod in alumnos:
                print(alumnos[cod])
            else:
                print("El alumno no existe")

        # 3. Añadir un alumno
        case 3:
            newCod = input("DAME CODIGO NUEVO: ")

            if newCod not in alumnos:
                nombre = input("DAME NOMBRE: ")
                edad = int(input("DAME EDAD: "))
                nota = float(input("DAME NOTA: "))

                alumnos[newCod] = {
                    "nombre": nombre,
                    "edad": edad,
                    "nota": nota
                }

                print("Alumno añadido correctamente")
            else:
                print("Ese codigo ya existe")

        # 4. Modificar nota
        case 4:
            cod = input("DIME EL CODIGO DEL ALUMNO: ")

            if cod in alumnos:
                nuevaNota = float(input("DAME LA NUEVA NOTA: "))

                alumnos[cod]["nota"] = nuevaNota

                print("Nota modificada correctamente")
            else:
                print("El alumno no existe")

        # 5. Eliminar alumno
        case 5:
            cod = input("DIME EL CODIGO DEL ALUMNO: ")

            if cod in alumnos:
                print("Has eliminado a:", alumnos[cod])
                alumnos.pop(cod)
            else:
                print("El alumno no existe")

        # 6. Calcular media
        case 6:
            if len(alumnos) > 0:
                sumanotas = 0

                for valor in alumnos.values():
                    sumanotas += valor["nota"]

                usuarios = len(alumnos)
                media = sumanotas / usuarios

                print("LA MEDIA ES:", media)
            else:
                print("No hay alumnos registrados")

        # 7. Mostrar alumnos con nota superior a 5
        case 7:
            for clave, valor in alumnos.items():
                if valor["nota"] > 5:
                    print(clave, valor)

        # 8. Contar alumnos
        case 8:
            print("NUMERO DE ALUMNOS:", len(alumnos))

        # 9. Salir
        case 9:
            print("Saliendo del programa...")

        # Opción incorrecta
        case _:
            print("Opcion no valida")
