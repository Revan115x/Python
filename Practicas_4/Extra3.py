"""Apartados:
1. Recorre el diccionario y muestra todos los alumnos con sus notas.
2. Calcula la media de todas las notas.
3. Muestra los alumnos que han aprobado (nota igual o superior a 5).
4. Muestra los alumnos que han suspendido.
5. Pregunta por un alumno y una nueva nota, y actualiza su nota.
6. Muestra el alumno con la nota más alta.

RECORRER · ACUMULAR · CALCULAR · ACTUALIZAR"""

notas = {
    "Ana": 8.5,
    "Juan": 4.2,
    "Maria": 9.0,
    "Pedro": 6.5,
    "Lucia": 3.8
}

for clave, valor in notas.items():
    print(clave, valor)
    
suma = sum(notas.values())
alum = len(notas)

media = suma / alum

for clave, valor in notas.items():
    if valor >= 5:
        print("Alum aprobado ",clave)

for clave, valor in notas.items():
    if valor < 5:
        print("Alum aprobado ",clave)

nombre = input("NOMBRE ALUMNO :")

if nombre in notas:
    nota = input("DIME SU NUEVA NOTA")
    notas[nombre]= nota
else:
    print("NO EXISTE")

print("Nota media ",media)
print("Nota Alumo",nombre," : ",notas.get(nombre))