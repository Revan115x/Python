# AÑADIR Y MODIFICAR
agenda = {"Ana": "611111111"}

agenda["Luis"] = "622222222"  # Añade Luis.
agenda["Ana"] = "699999999"   # Modifica el teléfono de Ana.

print(agenda)
# SALIDA:
# {'Ana': '699999999', 'Luis': '622222222'}

# NO CONFUNDIR:
# agenda = {"nombre": nombre, "telefono": telefono}
# crea/reemplaza un diccionario con esas claves literales.
# agenda[nombre] = telefono
# añade o actualiza una entrada dentro del diccionario existente.
