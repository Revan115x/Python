# CREAR UN CONJUNTO
numeros = {1, 2, 3, 4, 5}

print(numeros)

# CREAR UN CONJUNTO VACIO
vacio = set()

# CREAR CONJUNTO DESDE UNA LISTA
datos = set([1, 2, 2, 3, 3, 4])

print(datos)

# AÑADIR UN ELEMENTO
colores = {"rojo", "azul"}

colores.add("verde")

print(colores)

# AÑADIR VARIOS ELEMENTOS
numeros = {1, 2, 3}

numeros.update([4, 5, 6])

print(numeros)

# ELIMINAR CON REMOVE
animales = {"perro", "gato", "conejo"}

animales.remove("gato")

print(animales)

# ELIMINAR CON DISCARD
animales.discard("caballo")

print(animales)

# ELIMINAR CON POP
eliminado = animales.pop()

print(eliminado)
print(animales)

# COMPROBAR PERTENENCIA
print("perro" in animales)
print("gato" not in animales)

# UNION
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)

# INTERSECCION
print(A & B)

# DIFERENCIA
print(A - B)
print(B - A)