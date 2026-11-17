"""Apartados:
1. Convierte todo el texto a minúsculas.
2. Separa el texto en palabras utilizando split().
3. Crea un diccionario vacío.
4. Recorre la lista de palabras.
5. Si la palabra no existe en el diccionario, añádela con valor 1.
6. Si ya existe, aumenta su contador en 1.
7. Muestra el diccionario final.

DICCIONARIOS DESDE CERO · FRECUENCIAS"""

texto = "Python es genial y Python es divertido"

nuevoTexto = texto.upper()

diccionario = {}
lista = nuevoTexto.split()

for i in range (0 , len(lista)):
    diccionario[lista[i]] = lista.count(lista[i])

print(diccionario)