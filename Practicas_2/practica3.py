"""Ejercicio 3. Representación de números y conversiones de base
Pide un número entero al usuario mediante teclado. Muestra su representación en diferentes sistemas de numeración
utilizando las funciones integradas de Python:
Representación binaria con bin() .
Representación octal con oct() .
Representación hexadecimal con hex() .
Desafío opcional: Convierte una cadena binaria introducida por el usuario (ej. "0b10101" ) de nuevo a un entero
utilizando int(cadena, 2) ."""

n1 = int(input("Dime un número entero: "))

print("Binario:", bin(n1))
print("Octal:", oct(n1))
print("Hexadecimal:", hex(n1))