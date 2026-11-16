"""1. Lee por teclado números y guardalo en una lista, el proceso finaliza cuando
metamos un número negativo. Muestra el máximo de los números guardado en la
lista, muestra los números pares."""

numeros = []

num = int(input("DIME UN NUMERO: "))

while num >= 0:

    numeros.append(num)

    num = int(input("DIME OTRO NUMERO: "))

print(numeros)