# 14 - Diccionarios anidados

alumnos = {
    "A01": {"nombre": "Lucia", "edad": 20, "nota": 8},
    "A02": {"nombre": "Mario", "edad": 22, "nota": 6}
}

# Acceder a un dato interior
print(alumnos["A01"]["nota"])

# Recorrer código y datos del alumno
for codigo, datos in alumnos.items():
    print("Código:", codigo)
    print("Nombre:", datos["nombre"])
    print("Edad:", datos["edad"])
    print("Nota:", datos["nota"])

# Modificar una nota
alumnos["A01"]["nota"] = 9
