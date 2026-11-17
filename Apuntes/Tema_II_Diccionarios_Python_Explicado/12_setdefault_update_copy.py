# 12 - setdefault(), update() y copy()

datos = {"Ana": 8}

# Si Ana existe, devuelve su valor sin cambiarlo.
print(datos.setdefault("Ana", 0))
print(datos)

# Si Luis no existe, lo añade con el valor indicado.
print(datos.setdefault("Luis", 6))
print(datos)

# update añade o actualiza varias parejas.
datos.update({"Marta": 9, "Ana": 10})
print(datos)

# copy crea otro diccionario (copia superficial).
copia = datos.copy()
copia["Ana"] = 4
print("Original:", datos)
print("Copia:", copia)
