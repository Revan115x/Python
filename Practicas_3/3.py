"""3. Dada una lista de cadenas, pide una cadena por teclado e indica si está en la lista,
indica cuantas veces aparece en la lista, lee otra cadena y sustituye la primera por la
segunda en la lista, y por último borra la cadena de la lista"""

lista = ["arroz","pollo","leche","agua"]

cadena = input ("Producto : ")

if cadena in lista :
    print("Esta cade si existe")
    posicion = lista.index(cadena)
else:
    print("No existe")

print("Aparece una cantidad de : ", lista.count(cadena))

cadena = input ("Producto : ")

lista[posicion] = cadena

print(lista)

lista.remove(cadena)

print(lista)