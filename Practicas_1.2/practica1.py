"""Ejercicio 1. Entrada y salida personalizada con separadores
Escribe un programa en Python que pida al usuario su nombre y su edad mediante la función input() . A continuación,jose
muestra un mensaje de bienvenida en la consola con la función print() cumpliendo las siguientes condiciones:
Usa el parámetro sep=" - " para separar el texto y los valores.
Usa el parámetro end=".\n" para finalizar la línea con un punto y un salto de línea."""

nombre=input("Nombre?")
edad=input("edad?")

print("Bienvenido", nombre, "- tienes", edad, "años", sep=" - ", end=".\n")