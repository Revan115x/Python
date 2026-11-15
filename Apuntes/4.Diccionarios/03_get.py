# GET: CONSULTAR UNA CLAVE SIN KEYERROR

producto = {"nombre": "Portátil", "precio": 800}

print(producto.get("nombre"))
print(producto.get("fabricante"))
print(producto.get("fabricante", "No indicado"))
