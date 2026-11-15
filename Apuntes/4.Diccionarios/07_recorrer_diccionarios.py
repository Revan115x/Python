# RECORRER CLAVES, VALORES Y PAREJAS

persona = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Madrid"
}

print("CLAVES")
for clave in persona:
    print(clave)

print("VALORES")
for valor in persona.values():
    print(valor)

print("CLAVE Y VALOR")
for clave, valor in persona.items():
    print(clave, valor)
