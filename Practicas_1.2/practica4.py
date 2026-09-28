"""Ejercicio 4. Repartidor de caramelos (División entera y módulo)
Escribe un programa que solicite el número total de caramelos repartidos en un evento y el número de asistentes.
Utiliza la función predefinida divmod(x, y) para obtener la división entera y el resto en una sola instrucción.
Desempaqueta la tupla devuelta e imprime cuántos caramelos recibe cada participante y cuántos sobran en la caja."""

def repartir_caramelelos(nCaramelos, nAsistentes):
    caramelosPorPersona, caramelosSobran = divmod(nCaramelos, nAsistentes)
    return caramelosPorPersona, caramelosSobran


nCaramelos = int(input("Dime la cantidad de caramelos: "))
nAsistentes = int(input("Dime la cantidad de asistentes: "))

porPersona, sobran = repartir_caramelelos(nCaramelos, nAsistentes)

print("Cada participante recibe", porPersona, "caramelos")
print("Sobran", sobran, "caramelos en la caja")