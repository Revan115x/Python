# 09 - Objetos mutables e inmutables

# Numeros y cadenas: inmutables.
numero = 5
texto = "Hola"

# No se puede cambiar un caracter de una cadena:
# texto[0] = "h"  # TypeError

# Para obtener otro texto, asignamos una nueva cadena.
texto = "hola"
print(texto)

# Las listas son mutables.
a = [1, 2]
b = a  # b apunta a la misma lista que a

print("Identificador a:", id(a))
print("Identificador b:", id(b))

a[0] = 5
print("a:", a)
print("b:", b)

# Una lista creada por separado es otro objeto.
c = [1, 2]
print("a y c tienen el mismo contenido:", a == c)
print("a y c son el mismo objeto:", a is c)
