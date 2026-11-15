# OPERACIONES DE CONJUNTOS SOBRE KEYS

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 4}

# Intersección: claves comunes
print(dict1.keys() & dict2.keys())

# Unión: todas las claves sin repetir
print(dict1.keys() | dict2.keys())

# Diferencia: claves que solo están en dict1
print(dict1.keys() - dict2.keys())

# Diferencia simétrica: claves que no están en ambos
print(dict1.keys() ^ dict2.keys())
