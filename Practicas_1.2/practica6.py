"""Ejercicio 6. Manipulación y formateo de cadenas
Pide al usuario que introduzca su nombre completo en minúsculas (ejemplo: "juan carlos pérez" ).
Muestra la cadena convertida a formato título mediante el método .title() .
Muestra la longitud total del nombre utilizando len() .
Divide el nombre en palabras individuales usando el método .split(' ') e imprime la lista resultante."""

nombre = str(input("Nombre completo: "))

print(nombre.title())

print(len(nombre))

print(nombre.split(' '))