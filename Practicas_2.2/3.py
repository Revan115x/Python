"""Crea tres programas independientes utilizando la instrucción match-case :
Dado un entero x , utiliza un patrón múltiple ( case 10 | 20 | 30: ) para imprimir f"Matched: {x}" , y un caso
comodín ( case _: ) para imprimir "No match found" .
Dada una lista data , utiliza patrones de listas para identificar si contiene dos elementos ( case [x, y]: ) o tres
elementos ( case [x, y, z]: ), imprimiendo los elementos capturados. Incluye el caso comodín para formatos
desconocidos.
Dado un entero x , utiliza una guarda en el patrón ( case 10 if x % 2 == 0: ) para verificar si es 10 y además es
par, otro patrón para 10 no par y la opción por defecto."""


numero = input(print("Numero"))

match numero:
    case 10|20|30:
        print("Matched: "+numero)
    case _:
        print("No match found")