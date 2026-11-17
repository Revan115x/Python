# 02 - Consultar valores con [] y get()

agenda = {
    "Ana": "600111222",
    "Luis": "600333444"
}

# Consultar con corchetes: la clave debe existir
print(agenda["Ana"])

# get() devuelve None si la clave no existe
print(agenda.get("Pedro"))

# get() permite indicar un texto alternativo
print(agenda.get("Pedro", "Contacto no encontrado"))

# Comprueba qué ocurre si descomentas la siguiente línea:
# print(agenda["Pedro"])  # KeyError
