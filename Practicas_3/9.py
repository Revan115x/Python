"""9. Simula el juego de la lotería primitiva:
a) Dibuja el boleto (sólo uno)
b) Pide al usuario que introduzca sus números elegidos
c) Realiza el sorteo
d) Comprueba el boleto del usuario"""

import random

for i in range(1, 50):
    print(i,end=" ")

    if i % 7 == 0:
        print("")
boleto = []
boletoGanador = []

for i in range (1,7):

    numero = int(input("DIME TU NUMEROS "))

    while numero in boleto:
        print("Ese número ya existe")
        numero = int(input("Introduce otro número: "))

    boleto.append(numero)

for i in range (1,7):

    ganador = random.randint(1, 49)

    while ganador in boletoGanador:
        ganador = random.randint(1, 49)

    boletoGanador.append(ganador)

aciertos = 0

for numero in boleto:
    if numero in boletoGanador:
        print("Has acertado el número: ",numero)
        aciertos += 1

print("Total de aciertos: ",aciertos)

if aciertos == 6 :
    print("PREMIO MAXIMO")
elif aciertos < 3 : 
    print("SUERTE LA PROXIMA") 

print(boleto)
print(boletoGanador)

