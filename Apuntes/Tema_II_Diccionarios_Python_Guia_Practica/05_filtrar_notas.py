# APROBADOS, SUSPENSOS Y MEDIA
notas = {"Ana": 8, "Luis": 4, "Marta": 9, "Pablo": 3}

print("APROBADOS:")
for alumno, nota in notas.items():
    if nota >= 5:
        print(alumno, nota)
# SALIDA:
# APROBADOS:
# Ana 8
# Marta 9

print("SUSPENSOS:")
for alumno, nota in notas.items():
    if nota < 5:
        print(alumno, nota)
# SALIDA:
# SUSPENSOS:
# Luis 4
# Pablo 3

suma = 0
for nota in notas.values():
    suma += nota
print("MEDIA:", suma / len(notas))
# SALIDA: MEDIA: 6.0
