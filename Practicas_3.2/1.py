"""1. El filtro del club de baile
Organizas una fiesta para 25 personas, abres un formulario para que se apunte
todo el que quiera, una persona puede apuntarse varias veces. Cuando cierras
fecha:
a. Elimina a los repetidos dejando solo una vez a cada persona
b. Ordena la lista de invitados alfabéticamente.
c. Si se ha superado el aforo, genera una letra aleatoriamente y crea una
nueva lista con los nombres que empiecen con esa letra o posteriores. Si
sigue habiendo más de 50 personas, genera otra letra posterior a la
anterior y repite el proceso... Lo harás tantas veces como sea necesario.
Genera una lista con todas las personas que se van quedando fuera de la
fiesta. Si en el último descarte, no se llega a 25 personas, irás sacando de
la lista de “espera” hasta completar el aforo.
d. Imprime el mensaje: «Los elegidos de la fiesta son: [...]»."""

Lista = ["MARIA","JUAN","ANA","TERESA","HECTOR","KEVIN","MIGUEL","ZARA","YODA","LUKE","BALDUR"]
invitados = []
import random
import string

for i in range(0,5):
    nombre = input("NOMBRE DEL INVITADO : ")
    print("Invitado agregado")
    Lista.append(nombre)

for i in Lista:
    if i not in invitados:
        invitados.append(i)

invitados.sort()
print("Lista de Invitados")
print(invitados)

letra = random.choice(string.ascii_uppercase)
print(letra)
nuevalista = []
listaEspera = []

for i in invitados:
    nombre = i
    if nombre[0] >= letra:
        print(nombre)
        nuevalista.append(nombre)
    else :
        listaEspera.append(nombre)

ListaInvitados = []

while len(nuevalista) > 50:

    # Buscar las letras posteriores a la que ya tenemos
    letrasPosteriores = string.ascii_uppercase[string.ascii_uppercase.index(letra) + 1:]

    # Si no quedan letras posteriores, terminamos
    if len(letrasPosteriores) == 0:
        break

    # Elegir una nueva letra posterior
    letra = random.choice(letrasPosteriores)
    print("Nueva letra:", letra)

    # Lista temporal para los que pasan esta ronda
    nuevaRonda = []

    # Recorrer solamente los invitados que pasaron la ronda anterior
    for nombre in nuevalista:

        if nombre[0] >= letra:
            nuevaRonda.append(nombre)
        else:
            listaEspera.append(nombre)

    # Actualizar los invitados que siguen participando
    nuevalista = nuevaRonda

print("------------------------------------------------------------------j")
print(nuevalista)