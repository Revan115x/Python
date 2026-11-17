# 10 - Recorrer un diccionario y guardar coincidencias en una lista

inventario = {
    "Minecraft": 10,
    "Zelda": 5,
    "Mario": 8,
    "Pokemon": 3
}

juegos_con_stock = []

for nombre, cantidad in inventario.items():
    if cantidad >= 5:
        juegos_con_stock.append(nombre)

print("Lista:", juegos_con_stock)
print("Como texto:", ", ".join(juegos_con_stock))
