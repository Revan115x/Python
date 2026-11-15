from funciones import *

tipo_entrada = ["Normal", "VIP", "Backstage"]
precios = (50, 120, 200)
stock_entradas = {"Normal": 100,"VIP": 30,"Backstage": 10}
precios_entrada = dict(zip(tipo_entrada, precios))
asistentes = {}
asistentes_dentro = set()

grupo_prueba = [
    {"dni": "12345678Z", "nombre": "Lucia", "edad": 20, "entrada": "Normal"},
    {"dni": "87654321X", "nombre": "Carlos", "edad": 22, "entrada": "VIP"},
    {"dni": "11111111H", "nombre": "Marta", "edad": 19, "entrada": "Backstage"}
]
grupo_prueba_2 = [
    {
        "dni": "44444444A",
        "nombre": "Alejandro",
        "edad": 25,
        "entrada": "VIP"
    },
    {
        "dni": "55555555B",
        "nombre": "Elena",
        "edad": 30,
        "entrada": "VIP"
    }
]

grupo_prueba_3 = [
    {
        "dni": "99999999Z",
        "nombre": "Pablo",
        "edad": 18,
        "entrada": "Normal"
    },
    {
        "dni": "88888888Y",
        "nombre": "Sofia",
        "edad": 21,
        "entrada": "Backstage"
    },
    {
        "dni": "77777777X",
        "nombre": "David",
        "edad": 24,
        "entrada": "Normal"
    }]
grupo_error_edad = [
    {
        "dni": "11223344A",
        "nombre": "Carlos",
        "edad": 22,
        "entrada": "Normal"
    },
    {
        "dni": "55667788B",
        "nombre": "Marcos",
        "edad": 16,  # <-- Provoca EdadInvalidaError
        "entrada": "VIP"
    }
]

grupo_error_dni = [
    {
        "dni": "1234A",  # <-- Provoca DniInvalidaError (no tiene 9 caracteres)
        "nombre": "Lucía",
        "edad": 20,
        "entrada": "Normal"
    }
]

grupo_error_duplicado = [
    {
        "dni": "99887766Z",
        "nombre": "Sara",
        "edad": 25,
        "entrada": "Backstage"
    },
    {
        "dni": "99887766Z",  # <-- Provoca AsistenteYaRegistradoError (DNI repetido)
        "nombre": "Sara",
        "edad": 25,
        "entrada": "Backstage"
    }
]

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
                mostrar_entradas(stock_entradas, precios_entrada)
                
            case "2":
                try:
            
                    comprar_entradas(grupo_prueba, asistentes, stock_entradas, precios_entrada)
                    comprar_entradas(grupo_prueba_2, asistentes, stock_entradas, precios_entrada)
                    comprar_entradas(grupo_prueba_3, asistentes, stock_entradas, precios_entrada)
                    comprar_entradas(grupo_error_edad, asistentes, stock_entradas, precios_entrada)
                    comprar_entradas(grupo_error_dni, asistentes, stock_entradas, precios_entrada)
                    comprar_entradas(grupo_error_duplicado, asistentes, stock_entradas, precios_entrada)

                except Exception as error:
                    print("Error:", error)
                    
            case "3":
                dni = input("DNI del asistente: ").upper()

                try:
                    info_asistente(dni, asistentes)
                except AsistenteNoRegistradoError as error:
                    print(error)

            case "4":
                dnis_prueba_acceso = [
                    "12345678Z",  # OK: Lucía entra (registrada en grupo_prueba)
                    "44444444A",  # OK: Alejandro entra (registrado en grupo_prueba_2)
                    "12345678Z",  # ERROR: Lucía intenta entrar otra vez (ya está dentro)
                    "55667788B"   # ERROR: Marcos (no registrado, su compra fue rechazada por ser menor)
                ]
                for dni in dnis_prueba_acceso:
                    print("Probandocontrol de acceso para DNI", {dni})
                    try:
                        controlar_acceso( dni, asistentes,asistentes_dentro)
                    except Exception as error:
                        print("Acceso denegado:", error)

            case "5":
                print("Asistentes registrados:", len(asistentes))
                print("Personas dentro:" , len(asistentes_dentro))
                print("Entradas disponibles:", sum(stock_entradas.values()))

            case "0":
                print("Gracias por usar NEON FEST")
                break

            case _:
                print("Opción incorrecta.")
                
menu()