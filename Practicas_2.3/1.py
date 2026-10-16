"""Escribe una función que pinta un rectángulo en función de su altura y anchura. Opcionalmente
se puede pasar el carácter con el que pintará"""


columnas = int(input("Número de columnas: "))
filas = int(input("Número de filas: "))

def pintar(f, c, caracter="*"):
    for i in range(f):
        for a in range(c):
            print(caracter, end="")
        print()

pintar(filas, columnas)