# CONSULTAR UN VALOR DE UN DICCIONARIO
agenda = {"Ana": "611111111", "Luis": "622222222"}

# Opción 1: corchetes. Úsalo si sabes que la clave existe.
print(agenda["Ana"])
# SALIDA: 611111111

# Opción 2: get(). Si no existe, devuelve None.
print(agenda.get("Pedro"))
# SALIDA: None

# Opción 3: get() con mensaje alternativo.
print(agenda.get("Pedro", "NO ENCONTRADO"))
# SALIDA: NO ENCONTRADO
