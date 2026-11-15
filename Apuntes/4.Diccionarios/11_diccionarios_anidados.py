# DICCIONARIOS CON LISTAS Y OTROS DICCIONARIOS

persona = {
    23: {
        "nombre": "Michael",
        "equipo": "Chicago",
        "anillos": {
            "temporadas": [1991, 1992, 1993, 1996, 1997, 1998]
        }
    }
}

print(persona[23]["nombre"])
print(persona[23]["equipo"])
print(persona[23]["anillos"]["temporadas"])
print(persona[23]["anillos"]["temporadas"][0])
