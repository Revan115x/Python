"""2. El chismoso del grupo
Dos grupos de amigos hicieron una lista de videojuegos que les gustan
a. ¿Qué juego les gusta a todos?
b. ¿Cuáles son todos los juegos únicos que les gustan entre los dos grupos?
c. ¿Qué juegos le gustan al Grupo A que no le gusten al Grupo B"""

GrupoA = ["BATMAN", "GTAV", "FIFA", "CALLOFDUTY", "GODOFWAR"]

GrupoB = ["GTAV", "FIFA", "RESIDENTEVIL", "INFAMOUS", "FORTNITE"]

# Convertimos las listas en conjuntos
A = set(GrupoA)
B = set(GrupoB)

Comunes = A.intersection(B)

Unicos = A.union(B)

Nogustan = A.difference(B)

print("JUEGOS EN COMUN :",Comunes)
print("JUEGOS DIFERENTES :",Unicos)
print("JUEGOS QUE NO LE GUSTAN AL B DEL A: ",Nogustan)

