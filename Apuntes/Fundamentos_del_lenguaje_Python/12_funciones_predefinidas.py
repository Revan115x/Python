# 12 - Funciones predefinidas numericas y de cadenas

# Funciones numericas
print(abs(-5))           # 5
print(divmod(7, 2))      # (3, 1)
print(hex(15))           # 0xf
print(oct(8))            # 0o10
print(bin(5))            # 0b101
print(pow(2, 3))         # 8
print(round(7.567, 1))   # 7.6

# Funciones y metodos de cadenas
texto = "Hola Mundo"

print(len(texto))
print(min("casa"))         # a
print(max("casa"))         # s
print(texto.upper())       # HOLA MUNDO
print(texto.lower())       # hola mundo
print(texto.title())       # Hola Mundo

datos = "Ana,20,Madrid"
partes = datos.split(",")
print(partes)              # ['Ana', '20', 'Madrid']

frase = "uno dos tres"
print(frase.split())       # separa por espacios en blanco
