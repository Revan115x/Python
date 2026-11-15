# 07 - Cadenas, indices, slicing, chr y ord

palabra = "Python"

# Indices positivos
print(palabra[0])   # P
print(palabra[1])   # y

# Indices negativos
print(palabra[-1])  # n
print(palabra[-2])  # o

# Slicing: cadena[inicio:fin:paso]
print(palabra[1:4])   # yth
print(palabra[1:1])   # cadena vacia
print(palabra[2:])    # thon
print(palabra[:-2])   # Pyth
print(palabra[:])     # Python
print(palabra[0:6:2]) # Pto

print(chr(97))   # a
print(ord("a"))  # 97
