# RANGE DE 0 A 9
rango1 = range(10)

print(list(rango1))

# RANGE DE 1 A 10
rango2 = range(1, 11)

print(list(rango2))

# RANGE DE 5 EN 5
rango3 = range(0, 30, 5)

print(list(rango3))

# RANGE DE 3 EN 3
rango4 = range(0, 10, 3)

print(list(rango4))

# RANGE CON NUMEROS NEGATIVOS
rango5 = range(0, -10, -1)

print(list(rango5))

# UTILIZAR RANGE EN UN BUCLE
for i in range(5):
    print(i)

# UTILIZAR RANGE DE 1 A 5
for i in range(1, 6):
    print(i)

# UTILIZAR RANGE DE 2 EN 2
for i in range(0, 10, 2):
    print(i)

# FUNCIONES
rango = range(1, 11, 2)

print(len(rango))
print(max(rango))
print(min(rango))
print(sum(rango))
print(sorted(rango))

# ATRIBUTOS DE RANGE
print(rango.start)
print(rango.stop)
print(rango.step)