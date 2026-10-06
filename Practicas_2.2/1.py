"""Escribe scripts en Python para realizar el control de flujo sobre una variable numero :
Implementa una alternativa simple ( if ) que compruebe si numero < 0 e imprima "Número es negativo" .
Implementa una alternativa doble ( if-else ) que compruebe si numero < 0 e imprima "Número es negativo" , o
en caso contrario "Número es positivo" .
Implementa una alternativa múltiple ( if-elif-else ) que compruebe si el número es mayor que 0, menor que 0 o
igual a 0, imprimiendo el mensaje correspondiente en cada caso."""


numero = input("NUMERO")

if numero < 0 :
    print("NUMERO ES NEGATIVO")
elif numero > 0 :
    print("Número es positivo")
else :
    print("NUMERO ES 0")