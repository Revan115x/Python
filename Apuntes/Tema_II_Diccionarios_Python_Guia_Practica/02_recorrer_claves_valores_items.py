# LAS FORMAS DE RECORRER UN DICCIONARIO
notas = {"Ana": 8, "Luis": 4, "Marta": 9}

# 1) Directamente: la variable recibe las claves.
for alumno in notas:
    print(alumno)
# SALIDA:
# Ana
# Luis
# Marta

# 2) values(): la variable recibe solo los valores.
for nota in notas.values():
    print(nota)
# SALIDA:
# 8
# 4
# 9

# 3) items(): recibe clave y valor.
for alumno, nota in notas.items():
    print(alumno, "->", nota)
# SALIDA:
# Ana -> 8
# Luis -> 4
# Marta -> 9
