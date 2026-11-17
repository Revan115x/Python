# 06 - Recorrer solamente los valores

agenda = {
    "Ana": "600111222",
    "Luis": "600333444",
    "Marta": "600555666"
}

# En cada vuelta, telefono contiene un valor del diccionario.
for telefono in agenda.values():
    print(telefono)
