from funciones import *
from exceptions import *

# Lista (list) - Colección ordenada y modificable
tipo_entrada = ["Normal", "VIP", "Backstage"]

# Tupla (tuple) - Colección ordenada e inmutable
precios = (50, 120, 200)

# Diccionario (dict) - Colección de pares clave: valor
stock_entradas = {"Normal": 100, "VIP": 30, "Backstage": 10}

# Diccionario (dict) - Creado combinando la lista y la tupla
precios_entrada = dict(zip(tipo_entrada, precios))

# Diccionario (dict) - Almacenará los asistentes agrupados por DNI
asistentes = {}

# Conjunto (set) - Colección de elementos únicos para control de acceso rápida
asistentes_dentro = set()


def menu():
    while True:
        print("\n===== NEON FEST =====")
        print("1. Mostrar entradas")
        print("2. Comprar entradas")
        print("3. Consultar asistente")
        print("4. Control de acceso")
        print("5. Estadísticas")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                # Pasa diccionarios a la función
                mostrar_entradas(stock_entradas, precios_entrada)
                
            case "2":
                # Lista (list) - Almacenará temporalmente los datos del grupo de personas
                grupo = []
                try:
                    cantidad = int(input("¿Cuántas entradas quieres comprar?: "))
                    for i in range(cantidad):
                        print("\nPersona", i + 1)
                        dni = input("DNI: ").upper()
                        nombre = input("Nombre: ")
                        edad = int(input("Edad: "))
                        entrada = input("Tipo de entrada: ")

                        # Diccionario (dict) - Representa a una sola persona con sus atributos
                        persona = { "dni": dni, "nombre": nombre, "edad": edad, "entrada": entrada }
                        
                        # Añade el diccionario a la lista
                        grupo.append(persona)

                    # Pasa la lista y los diccionarios a la función
                    comprar_entradas(grupo, asistentes, stock_entradas, precios_entrada)

                except ValueError:
                    print("Debes introducir un número válido.")
                except Exception as error:
                    print("Error:", error)
                    
            case "3":
                dni = input("DNI del asistente: ").upper()

                try:
                    # Pasa el diccionario de asistentes a la función
                    info_asistente(dni, asistentes)
                except AsistenteNoRegistradoError as error:
                    print(error)

            case "4":
                dni = input("DNI para acceder: ").upper()
                try:
                    # Pasa el diccionario de asistentes y el conjunto a la función
                    controlar_acceso(dni, asistentes, asistentes_dentro)
                except Exception as error:
                    print("Acceso denegado:", error)

            case "5":
                print("Asistentes registrados:", len(asistentes))
                print("Personas dentro:", len(asistentes_dentro))
                print("Entradas disponibles:", sum(stock_entradas.values()))

            case "0":
                print("Gracias por usar NEON FEST")
                break

            case _:
                print("Opción incorrecta.")

menu()