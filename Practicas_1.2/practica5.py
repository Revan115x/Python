"""Ejercicio 5. Operadores de Identidad vs Igualdad ( == frente a is )
Crea un programa que defina las variables a = 256 y b = 256 , y las listas x = [1, 2] y y = [1, 2] .
Imprime el resultado de comparar a == b y a is b .
Imprime el resultado de comparar x == y y x is y .
Imprime los identificadores de memoria de cada objeto usando la función id() .
Añade un comentario en tu código explicando por qué a is b devuelve True mientras que x is y devuelve
False ."""

a = 256
b = 256

x = [1, 2]
y = [1, 2]

print(a == b)
print(a is b)

print(x == y)
print(x is y)

print(id(a))
print(id(b))
print(id(x))
print(id(y))

