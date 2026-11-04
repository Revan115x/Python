"""Crea una función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá H o l a , t ú
El usuario podrá indicar o no el número de espacios entre cada letra"""


cadena = input("dame una cadena de texto ")
espacios = int(input ("Dime los espacios que quieres "))
def parte (cadena,espacios):
    resultado = ""

    for letra in cadena:
        resultado = resultado + letra + " " * espacios

    return resultado

res = parte(cadena,espacios)

print(res)