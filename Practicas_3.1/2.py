# # 1. CREAR UNA LISTA
a = [1, 2, 3]

# 2. ASIGNACIÓN POR REFERENCIA
b = a

# 3. CREAR UNA COPIA DE LA LISTA
c = list(a)

b.append(4)
c.remove(2)
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")