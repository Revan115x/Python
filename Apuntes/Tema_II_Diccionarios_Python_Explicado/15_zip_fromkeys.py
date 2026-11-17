# 15 - Crear diccionarios con zip() y fromkeys()

nombres = ["Ana", "Luis", "Marta"]
telefonos = ["600111222", "600333444", "600555666"]

agenda = dict(zip(nombres, telefonos))
print(agenda)

asistencia = dict.fromkeys(nombres, False)
print(asistencia)
