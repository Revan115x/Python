"""1. Escribe un programa que lea una cadena y devuelva un diccionario con la
cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si
recibe “Qué lindo día que hace hoy” debe devolver: ‘que’: 2, ‘lindo’: 1,
‘día’: 1, ‘hace’: 1, ‘hoy’: 1"""

cadena = "Qué lindo día que hace hoy"

# quito
cadena = cadena.replace("é", "e")
cadena = cadena.replace("í", "i")
cadena = cadena.lower()
texto = cadena.split(" ")

cadena = list(texto)
diccionario = {}
print(texto)
for i in range (0 , len(cadena)):
    diccionario[cadena[i]] = cadena.count(cadena[i])

print(diccionario)