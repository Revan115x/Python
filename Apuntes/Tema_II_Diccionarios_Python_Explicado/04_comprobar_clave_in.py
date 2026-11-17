# 04 - in comprueba claves

agenda = {
    "Ana": "600111222",
    "Luis": "600333444"
}

nombre = input("Nombre que quieres buscar: ")

if nombre in agenda:
    print("Telefono:", agenda[nombre])
else:
    print("El contacto no existe")

# Para comprobar valores:
if "600111222" in agenda.values():
    print("El telefono está guardado")
