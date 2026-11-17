# BUSCAR Y MOSTRAR UN CONTACTO
agenda = {"Ana": "611111111", "Luis": "622222222"}
nombre = "Ana"

if nombre in agenda:
    print("NOMBRE:", nombre)
    print("TELEFONO:", agenda[nombre])
else:
    print("CONTACTO NO ENCONTRADO")

# SALIDA:
# NOMBRE: Ana
# TELEFONO: 611111111

# IMPORTANTE:
# agenda.keys() muestra TODAS las claves.
# agenda.get("telefono") busca una clave llamada literalmente "telefono".
# Si la clave es el nombre, consulta agenda.get(nombre).
