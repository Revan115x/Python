# 03 - Añadir y modificar con asignación mediante clave

agenda = {
    "Ana": "600111222",
    "Luis": "600333444"
}

# "Marta" no existe: se añade
agenda["Marta"] = "600555666"

# "Ana" ya existe: se modifica su teléfono
agenda["Ana"] = "699999999"

print(agenda)

# NO es lo mismo que crear otro diccionario:
# agenda = {"nombre": "Pedro", "telefono": "600777888"}
# Esa asignación reemplaza el diccionario asociado a agenda.
