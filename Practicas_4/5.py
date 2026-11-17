"""5. Suponga un diccionario que contiene como clave el nombre de una
persona y como valor una lista con todas sus “gustos”. Desarrolle un
programa que agregue “gustos” a la persona:
◦ Si la persona no existe la agregue al diccionario con una lista que
contiene un solo elemento.
◦ Si la persona existe y el gusto existe en su lista, no tiene ningún
efecto.
◦ Si la persona existe y el gusto no existe en su lista, agrega el gusto a la
lista.
Se deja de pedir personas cuando introducimos el carácter “*”.
La salida resultante debe escribirse

NOMBRE : PEPE
GUSTOS : VIAJAR , LEER , DEPORTE
NOMBRE : ANA
GUSTOS : VIAJAR , COMER

"""

personas = {}

while True:

    nombre = input("NOMBRE : ").upper()

    if nombre == "*":
        break

    gusto = input("GUSTO : ").upper()

    # Comprobamos si la persona ya existe
    if nombre in personas:

        # Comprobamos si el gusto ya está en su lista
        if gusto not in personas[nombre]:

            # Añadimos el gusto a su lista
            personas[nombre].append(gusto)

    else:
        # Si no existe, creamos la persona con una lista
        personas[nombre] = [gusto]


# Mostramos todas las personas y sus gustos
for nombre in personas:

    print("NOMBRE :", nombre)

    print("GUSTOS :", " , ".join(personas[nombre]))
