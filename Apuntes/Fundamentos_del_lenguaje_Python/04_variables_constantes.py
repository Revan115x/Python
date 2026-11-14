# 04 - Variables, None, del y anotaciones

dato = 5
print(dato, type(dato))

# Tipado dinamico: el tipo puede cambiar.
dato = "hola"
print(dato, type(dato))

resultado = None
print(resultado, type(resultado))

# Anotacion de tipo: no fuerza la conversion.
edad: int = 20
print(edad)

temporal = 100
del temporal
# print(temporal)  # NameError si se descomenta

# Mayusculas por convencion para constantes.
IVA = 0.21
precio = 100
print("Total:", precio + precio * IVA)
