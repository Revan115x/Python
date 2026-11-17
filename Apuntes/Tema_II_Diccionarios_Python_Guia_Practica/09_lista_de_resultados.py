# GUARDAR RESULTADOS DE UN RECORRIDO EN UNA LISTA
inventario = {"Minecraft": 10, "Zelda": 5, "Mario": 8}
juegos = []

for nombre, cantidad in inventario.items():
    if cantidad >= 8:
        juegos.append(nombre)

print(juegos)
# SALIDA: ['Minecraft', 'Mario']

# append([a, b]) mete una lista como UN elemento.
parejas = []
parejas.append(["Minecraft", 10])
print(parejas)
# SALIDA: [['Minecraft', 10]]
