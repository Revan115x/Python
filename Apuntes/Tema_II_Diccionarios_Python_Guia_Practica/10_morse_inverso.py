# BUSCAR LA CLAVE A PARTIR DE UN VALOR (MORSE)
codigo = {"A": ".-", "B": "-...", "C": "-.-."}
morse = "-... .-"
lista_morse = morse.split()
resultado = []

for codigo_actual in lista_morse:
    for letra, valor in codigo.items():
        if valor == codigo_actual:
            resultado.append(letra)

print("".join(resultado))
# SALIDA: BA

# Si coincide el VALOR, añadimos la CLAVE (letra).
# No uses codigo[valor]: eso buscaría una clave con ese texto.
