# SETDEFAULT Y UPDATE

persona = {"nombre": "Ana"}

# Como nombre existe, no cambia su valor.
print(persona.setdefault("nombre", "Luis"))

# Como edad no existe, se añade.
print(persona.setdefault("edad", 20))
print(persona)

# Añadir o actualizar varias parejas
persona.update({"ciudad": "Madrid", "edad": 21})
print(persona)

# También admite una lista de tuplas
persona.update([("curso", "DAW"), ("grupo", 2)])
print(persona)
