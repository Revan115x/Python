# POP, POPITEM, DEL Y CLEAR

datos = {"a": 1, "b": 2, "c": 3}

# pop elimina por clave y devuelve el valor
valor = datos.pop("b")
print("Valor eliminado:", valor)
print(datos)

# popitem elimina y devuelve la última pareja insertada
pareja = datos.popitem()
print("Pareja eliminada:", pareja)
print(datos)

# del elimina una clave concreta
del datos["a"]
print(datos)

# clear vacía todo el diccionario
datos.clear()
print(datos)
