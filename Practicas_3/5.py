"""5. Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n caracteres."""

lista = ["arroz","pollo","leche","agua","frijol","carne","pescado","verdura"]

n = 4

def filtrar_palabras(lista, n):
    palabras_filtradas = []
    for palabra in lista:
        if len(palabra) > n:
            palabras_filtradas.append(palabra)
    return palabras_filtradas

print(filtrar_palabras(lista, n))