# CREAR UNA TUPLA
tupla = ("Ana", "Luis", "Pedro", "Ana")

# MOSTRAR TUPLA
print(tupla)

# CREAR TUPLA VACIA
tupla_vacia = ()

# CREAR TUPLA CON tuple()
otra_tupla = tuple([1, 2, 3])

# ACCEDER A ELEMENTOS
print(tupla[0])
print(tupla[-1])

# COMPROBAR PERTENENCIA
print("Ana" in tupla)
print("Carlos" not in tupla)

# LONGITUD
print(len(tupla))

# MAXIMO Y MINIMO
numeros = (10, 20, 30, 40)

print(max(numeros))
print(min(numeros))

# SUMA
print(sum(numeros))

# CONTAR REPETICIONES
print(tupla.count("Ana"))

# CONCATENAR TUPLAS
a = (1, 2)
b = (3, 4)

print(a + b)

# REPETIR TUPLA
print(a * 3)

# ORDENAR (DEVUELVE UNA LISTA)
print(sorted(numeros))

# DESEMPAQUETAR TUPLA
mitupla = ("Ana", 12, 2, 1999)

nombre, dia, mes, anyo = mitupla

print(nombre)
print(dia)
print(mes)
print(anyo)