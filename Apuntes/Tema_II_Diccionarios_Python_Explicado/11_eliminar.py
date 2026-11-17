# 11 - Eliminar elementos

agenda = {
    "Ana": "600111222",
    "Luis": "600333444"
}

nombre = input("Contacto que quieres borrar: ")

if nombre in agenda:
    telefono_eliminado = agenda.pop(nombre)
    print("Se ha eliminado", nombre, telefono_eliminado)
else:
    print("El contacto no existe")

print(agenda)
