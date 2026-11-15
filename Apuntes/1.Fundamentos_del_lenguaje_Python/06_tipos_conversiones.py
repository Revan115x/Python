# 06 - Tipos de datos, conversiones y comprobaciones

entero = 7
real = 7.5
complejo = 1 + 2j
booleano = True
texto = "Python"

print(type(entero))
print(type(real))
print(type(complejo))
print(type(booleano))
print(type(texto))

# Conversiones
print(int(7.9))          # 7: elimina la parte decimal
print(int("345"))        # 345
print(float(1))          # 1.0
print(float("1.234"))    # 1.234
print(complex(2))        # (2+0j)
print(complex(2, 3))     # (2+3j)

# Comprobaciones de tipo
print(isinstance(5, int))      # True
print(isinstance(5.5, int))    # False

# print(int("123.3"))  # ValueError
print(float("123.3"))
