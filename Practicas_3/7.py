"""7. Implementar un sistema de nombres donde queremos identificar el nombre más
común. Pedimos al usuario que inserte los nombres ( -1 para terminar).
Rosa, Luis, Juan, Rosa, Rosa, Pepe, Luis
A continuación, se mostrará
Rosa: 3
Luis: 2
Juan: 1
Pepe:1"""

nombres = []

while True:

    nombre = input("DIME UN NOMBRE (-1 PARA TERMINAR): ")

    if nombre == "-1":
        break

    encontrado = False

    for elemento in nombres:

        if elemento[0] == nombre:
            elemento[1] += 1
            encontrado = True

    if encontrado == False:
        nombres.append([nombre, 1])


for elemento in nombres:
    print(elemento[0], ":", elemento[1])
