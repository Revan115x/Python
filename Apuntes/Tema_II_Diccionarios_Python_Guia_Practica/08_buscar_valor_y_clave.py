# COMPROBAR SI EXISTE UNA CLAVE O UN VALOR
agenda = {"Ana": "611111111", "Luis": "622222222"}

print("Ana" in agenda)  # Comprueba CLAVES.
# SALIDA: True

print("611111111" in agenda)  # No es una clave.
# SALIDA: False

print("611111111" in agenda.values())  # Comprueba VALORES.
# SALIDA: True
