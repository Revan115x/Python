# IN, NOT IN Y COPY

original = {"nombre": "Ana", "edad": 20}

print("nombre" in original)
print("ciudad" not in original)

# in busca claves, no valores
print("Ana" in original)  # False

copia = original.copy()
original["edad"] = 30

print("Original:", original)
print("Copia:", copia)
