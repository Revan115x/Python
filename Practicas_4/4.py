"""4. Escribir un programa que implemente una agenda. En la agenda se po-
drán guardar nombres y números de teléfono. El programa nos dará el

siguiente menú:
• Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en

la agenda, debe mostrar el teléfono y, opcionalmente, permitir modi-
ficarlo si no es correcto. Si el nombre no se encuentra, debe permitir

ingresar el teléfono correspondiente.
• Buscar: Nos pide una cadena de caracteres, y nos muestras todos los
contactos cuyos nombres comiencen por dicha cadena.
• Borrar: Nos pide un nombre y si existe nos preguntará si queremos
borrarlo de la agenda.
• Listar: Nos muestra todos los contactos de la agenda.
Implementar el programa con un diccionario."""


agenda = {"juan":"650558896"}

while True:

    print("\n===== AGENDA =====")
    print("1. Añadir / Modificar contacto")
    print("2. Buscar contacto")
    print("3. Borrar contacto")
    print("4. Listar contactos")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    match opcion:

        case "1":
            nombre = input("DIME EL NOMBRE DE USUARIO :")
            if nombre in agenda:
                print("TELEFONO:", agenda.get(nombre))
            else:
                print("NO EXISTE")
                telefono = input("NUMERO DE TELEFONO: ")
                agenda[nombre]=telefono
                print(agenda)
            pass

        case "2":
            nombre = input("DIME EL NOMBRE DE USUARIO :")
            if nombre in agenda:
                print("NOMBRE:", nombre)
                print("TELEFONO:", agenda.get(nombre))
            pass

        case "3":
            nombre = input("DIME EL NOMBRE DE USUARIO :")
            if nombre in agenda:
                agenda.pop(nombre)
                print("HAZ ELIMINADO A ",nombre," DE TU AGENDA DE CONTACTOS")
            else:
                print("NO EXISTE ESTE CONTACTO PARA ELIMINAR")
                break;
            pass

        case "4":
            for clave,valor in agenda.items():
                print("NOMBRE :", clave)
                print("TELEFONO", valor)
                print("-----------------")
            pass

        case "5":
            print("Saliendo de la agenda...")
            break

        case _:
            print("Opción no válida")
