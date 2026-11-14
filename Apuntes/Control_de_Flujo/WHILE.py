# TEMA 3 - BUCLE WHILE

# --------------------------------------------------
# EJEMPLO 1: repetir mientras se cumpla una condición
# --------------------------------------------------
año = 2001

while año <= 2005:
    print("Informes del año", año)
    año += 1

# Resultado:
# Informes del año 2001
# Informes del año 2002
# Informes del año 2003
# Informes del año 2004
# Informes del año 2005


# --------------------------------------------------
# EJEMPLO 2: while con else
# El else se ejecuta al terminar normalmente el bucle.
# --------------------------------------------------
numero = 1

while numero <= 3:
    print(numero)
    numero += 1
else:
    print("Hemos terminado")

# Resultado:
# 1
# 2
# 3
# Hemos terminado


# --------------------------------------------------
# EJEMPLO 3: while que termina con break
# El else NO se ejecuta cuando salimos con break.
# --------------------------------------------------
numero = 1

while numero <= 5:
    if numero == 3:
        break

    print(numero)
    numero += 1
else:
    print("Fin normal del bucle")

# Resultado:
# 1
# 2
