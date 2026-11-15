"""6. Haz un “motor de videojuegos” para dos personajes (pide los nombres por teclado):
a) Empieza el combate y se decide aleatoriamente quien empieza
b) Si ataca A restará su ataque a la defensa de B
c) Cambio de turno. B realiza el ataque.
d) Así hasta que un personaje sea derrotado.
Almacena en una sola lista el ataque y defensa de cada personaje (lista de listas). Los
ataques son aleatorios entre 1 y 10 y las defensas entre 1 y 15.
[[“nombre”, ataque,defensa], [“nombre,ataque,defensa]]"""
import random 

personaje1 = input("NOMBRE PERSONAJE1 = ")

ataque1 = random.randint(1, 10)
defensa1 = random.randint(1, 15)

personaje2 = input("NOMBRE PERSONAJE2 = ")

ataque2 = random.randint(1, 10)
defensa2 = random.randint(1, 15)

personajes = [
    [personaje1, ataque1, defensa1],
    [personaje2, ataque2, defensa2]
]

print("EMPIEZA EL COMBATE")
turno = random.randint(0, 1)

while personajes[0][2] > 0 and personajes[1][2] > 0:

    if turno == 0:

        print("Empieza", personajes[0][0])
        print(personajes[0][0], "ataca a", personajes[1][0])

        personajes[1][2] = personajes[1][2] - personajes[0][1]

    else:

        print("Empieza", personajes[1][0])
        print(personajes[1][0], "ataca a", personajes[0][0])

        personajes[0][2] =  personajes[0][2] -  personajes[1][1]

        print("Defensa de", personajes[0][0], ":", personajes[0][2])
    print("Defensa de", personajes[1][0], ":", personajes[1][2])

    turno = 1 - turno

if personajes[0][2] <= 0:
    print("Ganador:", personajes[1][0])
else:
    print("Ganador:", personajes[0][0])

print("personajes")