"""Programa que lea un carácter por teclado y compruebe si es una letra
mayúscula, minúscula o un dígito."""

caracter = input("Introduce un carácter: ")

if caracter.isupper():
    print("Es una letra mayúscula")
elif caracter.islower():
    print("Es una letra minúscula")
elif caracter.isdigit():
    print("Es un dígito")
else:
    print("No es una letra ni un dígito")