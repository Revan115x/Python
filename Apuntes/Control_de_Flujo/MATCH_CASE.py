# TEMA 3 - MATCH CASE
# match-case está disponible desde Python 3.10.

# --------------------------------------------------
# EJEMPLO 1: comparar distintos valores
# --------------------------------------------------
opcion = 2

match opcion:
    case 1:
        print("Inicio")
    case 2:
        print("Configuración")
    case 3:
        print("Salir")
    case _:
        print("Opción no válida")

# Resultado:
# Configuración


# --------------------------------------------------
# EJEMPLO 2: varios valores en un mismo case
# El símbolo | significa que puede coincidir con cualquiera.
# --------------------------------------------------
numero = 20

match numero:
    case 10 | 20 | 30:
        print("Número reconocido")
    case _:
        print("Número no reconocido")

# Resultado:
# Número reconocido


# --------------------------------------------------
# EJEMPLO 3: reconocer listas de dos o tres elementos
# --------------------------------------------------
datos = [10, 20]

match datos:
    case [x, y]:
        print("Dos elementos:", x, y)
    case [x, y, z]:
        print("Tres elementos:", x, y, z)
    case _:
        print("Formato desconocido")

# Resultado:
# Dos elementos: 10 20


# --------------------------------------------------
# EJEMPLO 4: patrón con condición adicional (guarda)
# --------------------------------------------------
numero = 10

match numero:
    case 10 if numero % 2 == 0:
        print("Es 10 y es par")
    case 10:
        print("Es 10, pero no es par")
    case _:
        print("No es 10")

# Resultado:
# Es 10 y es par
