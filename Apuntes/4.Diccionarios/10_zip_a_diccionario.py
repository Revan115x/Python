# CREAR UN DICCIONARIO CON ZIP

paises = ["Francia", "Alemania", "Italia"]
capitales = ["París", "Berlín", "Roma"]

diccionario = {}

for pais, capital in zip(paises, capitales):
    diccionario[pais] = capital

print(diccionario)
