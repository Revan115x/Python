"""Apartados:
1. Muestra todos los alumnos con su código, nombre, edad y nota.
2. Busca un alumno introduciendo su código.
3. Añade un alumno nuevo preguntando sus datos.
4. Modifica la nota de un alumno existente.
5. Elimina un alumno mediante su código.
6. Calcula la media de las notas de todos los alumnos.
7. Muestra los alumnos que tienen una nota superior a 5.
8. Muestra cuántos alumnos hay registrados."""

alumnos = {
    "A001": {
        "nombre": "Carlos",
        "edad": 20,
        "nota": 7.5
    },
    "A002": {
        "nombre": "Lucia",
        "edad": 21,
        "nota": 8.0
    },
    "A003": {
        "nombre": "Pedro",
        "edad": 19,
        "nota": 4.5
    }
}

print(alumnos," ")
encontrado = False

while encontrado != True:
    cod = input("DIME EL CODIGO DEL USUARIO : ")  

    if cod in alumnos:
        print(alumnos[cod])
        encontrado=True
    else:
        print("No existe")
        encontrado = False

newCod = input("DAME COD NUEVO USUARIO ")
nombre = input("DAME NOMBRE DE USUARIO ")
edad = input("DAME EDAD DE USUARIO ")
nota = input("DAME NOTA DE USUARIO ")

alumnos[newCod] = {"nombre": nombre,"edad":edad,"nota":nota}

for clave, valor in alumnos.items():
    print(clave,valor)


cod = input("DIME QUE ALUMNO QUIERES CAMBIAR NOTA :")
nuevaNota = input("nota :")

if cod in alumnos:
    alumnos[cod]["nota"] = nuevaNota
    print(alumnos[cod])


cod = input("DIME QUE ALUMNO QUIERES ELIMINAR :")

if cod in alumnos:
    print("Has eliminado a :", alumnos[cod])
    alumnos.pop(cod)

for clave, valor in alumnos.items():
    print(clave,valor)

sumanotas = 0

for valor in alumnos.values():
    sumanotas += valor["nota"] 

usuarios = len(alumnos)
media = sumanotas / usuarios

print("MEDIA ES DE : ", media)

for clave,valor in alumnos.items():
    if valor["nota"] >= 5:
        print("Alumnos aprobados ",clave,valor)

print(len(alumnos))