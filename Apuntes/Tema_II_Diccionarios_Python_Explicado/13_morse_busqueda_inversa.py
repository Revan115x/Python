# 13 - Buscar una clave a partir de un valor (Morse inverso)

morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "H": "....",
    "L": ".-..",
    "O": "---"
}

entrada = input("Introduce Morse separado por espacios: ")
codigos = entrada.split()
resultado = []

for codigo_actual in codigos:
    encontrado = False

    for letra, codigo in morse.items():
        if codigo == codigo_actual:
            resultado.append(letra)
            encontrado = True
            break

    if not encontrado:
        resultado.append("?")

texto = "".join(resultado)
print("Texto:", texto)

# Prueba: .... --- .-.. .-
# Resultado esperado: HOLA
