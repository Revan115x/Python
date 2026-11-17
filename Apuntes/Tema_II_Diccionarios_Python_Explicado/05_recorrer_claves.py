# 05 - Recorrer directamente el diccionario: claves

agenda = {
    "Ana": "600111222",
    "Luis": "600333444",
    "Marta": "600555666"
}

# En cada vuelta, nombre contiene una clave.
for nombre in agenda:
    print(nombre)

# Podemos usar esa clave para consultar el valor asociado.
for nombre in agenda:
    print("Nombre:", nombre, "| Telefono:", agenda[nombre])
