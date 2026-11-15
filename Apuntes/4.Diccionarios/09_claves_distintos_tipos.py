# LAS CLAVES NO TIENEN QUE SER STR

datos = {
    23: "Jordan",
    "Nombre": "Michael",
    "Equipo": "Chicago",
    (1, 2): "Coordenada"
}

print(datos[23])
print(datos["Nombre"])
print(datos[(1, 2)])

# Una lista no puede ser clave:
# datos[[1, 2]] = "No válido"
