"""Ejercicio 7. Extracción de subcadenas mediante Slicing ( cadena[i:j:k] )
Dada la variable texto = "FundamentosDePython" , realiza las siguientes operaciones e imprime los resultados:
Extrae la primera palabra ( "Fundamentos" ) utilizando rebanado positivo.
Extrae la palabra final ( "Python" ) utilizando únicamente índices negativos.
Obtén una cadena invertida ( "nohtyPeD sotnemadnuF" ) empleando un paso negativo.
Obtén una subcadena tomando únicamente un carácter de cada dos desde el inicio."""

texto = "FundamentosDePython"

# Primera palabra
print(texto[0:11])

# Palabra final utilizando únicamente índices negativos
print(texto[-6:])

# Cadena invertida
print(texto[::-1])

# Un carácter de cada dos desde el inicio
print(texto[::2])