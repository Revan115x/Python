# 09 - Buscar nombres que empiezan por unas letras

agenda = {
    "Ana": "600111222",
    "Antonio": "600222333",
    "Luis": "600333444",
    "Marta": "600555666"
}

inicio = input("Mostrar nombres que comiencen por: ")

for nombre, telefono in agenda.items():
    if nombre.lower().startswith(inicio.lower()):
        print(nombre, telefono)
