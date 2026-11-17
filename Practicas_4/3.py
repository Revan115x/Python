"""3. Continuar el programa: ahora nos pide un código morse donde cada letra
está separada por espacios y nos da la cadena correspondiente. Utilizar el
archivo con el código morse del ejercicio anterior"""

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

morse = input("DIME EL MORSE QUE QUIERES PASAR A TEXTO : ")
# SEPARO EL MORSE
lista_morse = morse.split()

# LISTA PARA GUARDAR EL RESULTADO
resultado = []

# RECCORE LOS CARACTERES DEL MORSE
for codigo_actual in lista_morse:

    # A LA VEZ RECORRO EL DIC
    for clave, valor in codigo.items():

        # SI EL VALOR DEL DIC ES IGUAL AL CARACTER
        if valor == codigo_actual:
            # GUARDO SU CLAVE EN EN MI LISTA
            resultado.append(clave)

# LO MUESTRO SIN []
print(" ".join(resultado))