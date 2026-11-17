# ENCONTRAR LA CLAVE QUE TIENE EL VALOR MÁS ALTO
notas = {"Ana": 8, "Luis": 4, "Marta": 9}

mayor = -1
mejor_alumno = ""

for alumno, nota in notas.items():
    if nota > mayor:
        mayor = nota
        mejor_alumno = alumno

print(mejor_alumno, mayor)
# SALIDA: Marta 9
