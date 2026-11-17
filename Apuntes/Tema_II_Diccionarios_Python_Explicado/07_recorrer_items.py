# 07 - Recorrer claves y valores con items()

agenda = {
    "Ana": "600111222",
    "Luis": "600333444",
    "Marta": "600555666"
}

# items() entrega parejas (clave, valor).
# Python reparte la pareja en nombre y telefono.
for nombre, telefono in agenda.items():
    print("Nombre:", nombre)
    print("Telefono:", telefono)
    print("--------------")
