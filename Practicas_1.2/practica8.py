"""Ejercicio 8. Conversión Unicode ( ord() y chr() )
Escribe un programa que realice dos operaciones de conversión de caracteres:
Pide una letra o símbolo al usuario y muestra su código punto de código Unicode utilizando ord() .
Pide un número entero entre 65 y 90 (caracteres ASCII mayúsculas) y muestra el carácter correspondiente usando
chr() ."""

letra=str(input("Letra:  "))

print(ord(letra))

num=int(input("Numero: "))


print(chr(num))