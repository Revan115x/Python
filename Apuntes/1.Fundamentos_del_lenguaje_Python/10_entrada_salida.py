# 10 - Entrada y salida estandar

# input devuelve una cadena.
nombre = input("Nombre: ")
print("Hola", nombre)

# Para utilizar un entero, convertimos el texto.
edad = int(input("Edad: "))
print("El año que viene tendras", edad + 1)

# Para decimales, usamos float.
precio = float(input("Precio: "))
print("Precio introducido:", precio)

# print separa varios valores con un espacio por defecto.
print(1, 2, 3)

# sep cambia el separador.
print(1, 2, 3, sep="-")

# end cambia el final (por defecto es salto de linea).
print("Primera parte", end=" ")
print("y segunda parte")

# str convierte un numero a cadena para concatenar.
cantidad = 6
print("Cantidad: " + str(cantidad))
