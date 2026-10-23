"""2. Escriba un programa que pida la anchura de un triángulo y lo dibuje. El usuario decidirá si con
el caracter por defecto * o cualquier otro. Utiliza dos funciones
*
* *
* * *
* *
*
"""

anchura = int(input("Numero de anchura "))
caracter = "{._.}"

def parte (anchura,caracter):
    for i in range(1, anchura + 1):
        for j in range(i):  # ¿Qué pondrías aquí?
            print(caracter, end=" ")
        print()