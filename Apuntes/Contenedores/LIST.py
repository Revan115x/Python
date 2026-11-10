# CREAR UNA LISTA
numeros = [10, 20, 30, 40, 50]

# MOSTRAR LA LISTA
print(numeros)

# ACCEDER A ELEMENTOS
print(numeros[0])       # Primer elemento
print(numeros[-1])      # Último elemento

# SUBLISTAS
print(numeros[1:3])     # Desde índice 1 hasta antes del 3
print(numeros[:])       # Lista completa

# LONGITUD
print(len(numeros))

# MINIMO, MAXIMO Y SUMA
print(min(numeros))
print(max(numeros))
print(sum(numeros))

# COMPROBAR SI EXISTE
print(20 in numeros)

# BUSCAR POSICION
print(numeros.index(30))

# CONTAR REPETICIONES
print(numeros.count(20))

# AÑADIR UN ELEMENTO
numeros.append(60)

# AÑADIR VARIOS ELEMENTOS
numeros.extend([70, 80])

# INSERTAR EN UNA POSICION
numeros.insert(0, 5)

# ELIMINAR POR VALOR
numeros.remove(30)

# ELIMINAR POR POSICION
numeros.pop()

# ORDENAR
numeros.sort()

# INVERTIR
numeros.reverse()

# MOSTRAR RESULTADO FINAL
print(numeros)