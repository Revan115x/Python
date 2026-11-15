# 08 - Operadores de Python

# Asignacion y asignacion abreviada
a = 10
a += 2
print("Despues de += 2:", a)

# Asignacion multiple
x, y, mensaje = 1, 2, "hola"
print(x, y, mensaje)

# Aritmeticos
print(4 + 3)   # 7
print(4 - 3)   # 1
print(4 * 3)   # 12
print(7 / 2)   # 3.5
print(7 // 2)  # 3
print(7 % 2)   # 1
print(2 ** 3)  # 8

# Comparacion y logicos
edad = 20
tiene_entrada = True
print(edad >= 18)  # True
print(edad == 15)  # False
print(edad >= 18 and tiene_entrada)
print(edad < 18 or tiene_entrada)
print(not tiene_entrada)

# Pertenencia
palabra = "Python"
print("P" in palabra)
print("z" not in palabra)

# Cadenas
print("Hola " + "DAW")
print("Ja" * 3)

# all y any
print(all([True, True, True]))
print(all([True, False, True]))
print(any([False, False, True]))
print(any([False, False]))

# Identidad: is comprueba si es el mismo objeto.
lista_a = [1, 2]
lista_b = lista_a
lista_c = [1, 2]
print(lista_a == lista_c)  # True: mismo contenido
print(lista_a is lista_b)  # True: mismo objeto
print(lista_a is lista_c)  # False: objetos distintos

# Operadores bit a bit
numero_a = 5  # 0101
numero_b = 3  # 0011
print(numero_a & numero_b)  # 1
print(numero_a | numero_b)  # 7
print(numero_a ^ numero_b)  # 6
print(numero_a << 1)        # 10
print(numero_a >> 1)        # 2
print(~numero_a)            # -6
