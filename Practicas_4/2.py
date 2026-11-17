"""Tenemos guardado en un diccionario los códigos morse correspondientes
a cada caracter(se almacenan como una constante en un archivo).
Escribir un programa que lea una palabra y la muestre usando el código
morse."""

codigo = {
'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..',
'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-',
'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..', '1': '.----',
'2': '..---', '3': '...--', '4': '....-',
'5': '.....', '6': '-....', '7': '--...',
'8': '---..', '9': '----.', '0': '-----',
'.': '.-.-.-', ',': '--..--', ':': '---...',
';': '-.-.-.', '?': '..--..', '!': '-.-.--',
'"': '.-..-.', "'": '.----.', '+': '.-.-.',
'-': '-....-', '/': '-..-.', '=': '-...-',
'_': '..--.-', '$': '...-..-', '@': '.--.-.',
'&': '.-...', '(': '-.--.', ')': '-.--.-'
}

texto = input("DIME EL TEXTO QUE QUIERES PASAR A MORSE : ")
# PASO EL TEXTO A MAYUSCULAS
texto = texto.upper()

# RESULTADO PARA MOSTRAR EL TEXTO EN MORSE
resultado = []

# RECORRO LAS LETRAS DEL TEXTO
for letra in texto:

    # SI LETRAS ESTAN EN CODIGO
    if letra in codigo:
        # AÑADO EL VALOR QUE TIENE EN EL DICCIONARIO EN RESULTADO
        resultado.append(codigo[letra])


# metodo join para mostrarlo sin los [] y devuelve un str
cadenaMorse= " ".join(resultado)

print(cadenaMorse)