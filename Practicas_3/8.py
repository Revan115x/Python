"""8. Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con
edades superiores a 20. Puedes variar el ejercicio para que sea el usuario quien ingrese
las edades."""

edades = (18, 25, 30, 16, 45, 22, 19, 35, 40, 17)

contador = 0

for edad in edades:

    if edad > 20:
        contador += 1

print("Personas mayores de 20:", contador)