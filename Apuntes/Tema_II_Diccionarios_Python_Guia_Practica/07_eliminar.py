# FORMAS DE ELIMINAR
agenda = {"Ana": "611", "Luis": "622"}

# del elimina una clave existente.
del agenda["Ana"]
print(agenda)
# SALIDA: {'Luis': '622'}

# pop elimina y devuelve el valor.
telefono = agenda.pop("Luis")
print(telefono)
print(agenda)
# SALIDA:
# 622
# {}
