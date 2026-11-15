# CREAR UN FROZENSET
numeros = frozenset([1, 2, 3, 4, 5])

# MOSTRAR CONJUNTO
print(" MOSTRAR CONJUNTO : ",numeros)

# COMPROBAR PERTENENCIA
print(" COMPROBAR PERTENENCIA ",3 in numeros)

# LONGITUD
print("LONGITUD ",len(numeros))

# MAXIMO Y MINIMO
print("MAXIMO ", max(numeros))
print("MINIMO ", min(numeros))

# SUMA
print("SUMA ",sum(numeros))

# UNION
A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])

print("UNION ",A | B)

# INTERSECCION
print("INTERSECCION ", A & B)

# DIFERENCIA
print("DIFERENCIA ",A - B)

# -----------------------------------------------------------------------------------

# CREAR UN FROZENSET CON TEXTOS
nombres = frozenset(["Ana", "Luis", "Pedro", "Maria", "Carlos"])

# MOSTRAR CONJUNTO
print("MOSTRAR CONJUNTO:", nombres)

# COMPROBAR PERTENENCIA
print("¿Está Ana?", "Ana" in nombres)

# LONGITUD
print("LONGITUD:", len(nombres))

# MÁXIMO Y MÍNIMO
print("MÁXIMO:", max(nombres))
print("MÍNIMO:", min(nombres))

# SUMA
# NO SE PUEDE UTILIZAR SUM() CON TEXTOS


# OPERACIONES ENTRE CONJUNTOS
A = frozenset(["Ana", "Luis", "Pedro"])
B = frozenset(["Pedro", "Maria", "Carlos"])

print("UNIÓN:", A | B)
print("INTERSECCIÓN:", A & B)
print("DIFERENCIA:", A - B)