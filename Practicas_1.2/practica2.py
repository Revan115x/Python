"""Ejercicio 2. Ticket de compra y formateo avanzado
Crea un script que pida el nombre de un producto, la cantidad comprada (entero) y el precio unitario en euros (flotante).
Calcula el total sin IVA y el total con un 21% de IVA aplicado.
Imprime el ticket formateado utilizando el método str.format() o f-strings.
Alinea el nombre del producto a la izquierda en un ancho de 15 caracteres ( {:15} ), la cantidad centrada en 5
espacios ( {:^5} ) y el precio final alineado a la derecha en 8 espacios con exactamente 2 decimales ( {:8.2f} )."""

nombre=input("nombre de un producto");
producto=int(input("Cantidad de Producto"))
precio_n=float(input("Precio Unidad"))

total= precio_n*producto

total_iva = total * 1.21

print("\n----- TICKET DE COMPRA -----")
print(f"{'Producto':15} {'Cantidad':^5} {'Precio':>8}")
print(f"{nombre:15} {producto:^5} {total_iva:8.2f} €")
print(f"Total sin IVA: {total:.2f} €")
print(f"Total con IVA (21%): {total_iva:.2f} €")