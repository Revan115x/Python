"""3. El traductor alienígena 
(Combinado: Listas + Tuplas + Conjuntos)
Un mensaje espacial ha sido interceptado. Viene en una lista de palabras, pueden
estar repetidas
a. Qué palabras dijeron los alienígenas
b. Convierte ese conjunto en una tupla ordenándola de alfabéticamente
(puedes usar sorted() que devuelve una lista y luego transformarla a
tupla).
c. Cuenta cuántas veces se repite la palabra "zorg" en la lista original
usando el método. count()."""

mensaje = ["zorg", "blip", "zorp", "zorg", "glorp", "blip", "nex", "zorg", "zorp", "plix", "glorp", "zorg", "blip"]

Set = set(mensaje)

nuevaTrupa = tuple(sorted(Set))

repeticiones = mensaje.count("zorg")

print("Mensaje sin palabras sin repetir ",nuevaTrupa)
print("zorg se repite : ",repeticiones)