# TEMA 3 - BREAK Y CONTINUE

# --------------------------------------------------
# EJEMPLO 1: break
# Termina el bucle cuando numero vale 3.
# --------------------------------------------------
for numero in range(1, 6):
    if numero == 3:
        break

    print(numero)

# Resultado:
# 1
# 2


# --------------------------------------------------
# EJEMPLO 2: continue
# Salta solamente la vuelta en la que numero vale 3.
# --------------------------------------------------
for numero in range(1, 6):
    if numero == 3:
        continue

    print(numero)

# Resultado:
# 1
# 2
# 4
# 5


# --------------------------------------------------
# EJEMPLO 3: break impide ejecutar el else del bucle
# --------------------------------------------------
for numero in range(1, 6):
    if numero == 3:
        break
    print(numero)
else:
    print("El bucle terminó normalmente")

# Resultado:
# 1
# 2
# No aparece el mensaje del else
