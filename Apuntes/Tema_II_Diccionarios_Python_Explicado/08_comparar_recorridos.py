# 08 - Comparación de recorridos

notas = {
    "Ana": 8,
    "Luis": 6,
    "Marta": 9
}

print("1) Claves:")
for clave in notas:
    print(clave)

print("\n2) Valores:")
for valor in notas.values():
    print(valor)

print("\n3) Claves y valores:")
for clave, valor in notas.items():
    print(clave, "->", valor)

print("\n4) Clave y consulta posterior:")
for clave in notas:
    print(clave, "->", notas[clave])
