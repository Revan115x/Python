""""""

datos = ["DAW", 10, 20.5, ["Python", "Java", "C++"], True, "Salesianas"]
# Responde qué devuelve cada expresión:


# lista[inicio:final:paso]
# inicio	Desde dónde empieza
# final	Dónde termina (sin incluirlo)
# paso	Cuántas posiciones avanza
# el índice final NUNCA se incluye.
p1 = datos[1:4] 

# ---------------------------------------
# Lista [posicion]:[dato] --> en esta caso una lista de listas
p2 = datos[3][1]

# ---------------------------------------
# lista a la inversa 
# 0	-6	"DAW"
# 1	-5	10
# 2	-4	20.5
# 3	-3	Lista interior [Python,Java,C++]
# 4	-2	True
# 5	-1	"Salesianas"
p3 = datos[-2:]

# ---------------------------------------
# lista dando saltos
# 0	"DAW"	Sí
# 1	10	No
# 2	20.5	Sí
# 3	Lista interior	No
# 4	True	Sí
# 5	"Salesianas"	No
p4 = datos[::2]

# Apend() crea una lista de lista 
# datos.append(["HTML", "CSS"])
# ["DAW", 10, 20.5, ["HTML", "CSS"]]
# extend() agrega el elemento a continuacion sin
# datos.extend(["HTML", "CSS"])
# ["DAW", 10, 20.5, "HTML", "CSS"]
datos[3].append("SQL")


p5 = datos[3]

print("P1 DEVUELVE =", p1)
print("P2 DEVUELVE =", p2)
print("P3 DEVUELVE =", p3)
print("P4 DEVUELVE =", p4)
print("P4 DEVUELVE =", p5)
