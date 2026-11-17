"""Apartados:
1. Pregunta al usuario qué videojuego quiere consultar.
2. Comprueba si existe en el inventario.
3. Si existe, muestra cuántas unidades quedan.
4. Si no existe, muestra "Producto no encontrado".
5. Recorre el diccionario mostrando cada videojuego y sus unidades.
6. Muestra únicamente los nombres de los videojuegos.
7. Muestra únicamente las cantidades.

GET · IN · KEYS · VALUES · ITEMS"""

inventario = {
    "Minecraft": 10,
    "Zelda": 5,
    "Mario": 8,
    "Pokemon": 3
}

nombre: str = input("nombre videojuego " )

if nombre in inventario:
    print(inventario[nombre])
else:
    print("Producto no encontrado")

print("NOMBRE VIDEOJUEGOS :",inventario.keys())
print("CANTIDAD VIDEOJUEGOS :",inventario.values())
