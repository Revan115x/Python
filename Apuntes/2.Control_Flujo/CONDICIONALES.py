# TEMA 3 - CONDICIONALES
# Ejecuta cada ejemplo por separado para practicar.

# --------------------------------------------------
# EJEMPLO 1: alternativa simple (if)
# --------------------------------------------------
numero = -5

if numero < 0:
    print("El número es negativo")

# Resultado:
# El número es negativo


# --------------------------------------------------
# EJEMPLO 2: alternativa doble (if-else)
# --------------------------------------------------
edad = 17

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Resultado:
# Eres menor de edad


# --------------------------------------------------
# EJEMPLO 3: alternativa múltiple (if-elif-else)
# --------------------------------------------------
nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

# Resultado:
# Notable


# --------------------------------------------------
# EJEMPLO 4: expresión reducida del if
# --------------------------------------------------
idioma = "es"

saludo = "HOLA" if idioma == "es" else "HI"

print(saludo)

# Resultado:
# HOLA
