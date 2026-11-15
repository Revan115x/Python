# 05 - Importar constantes desde otro modulo
# Mantener constantes.py en la misma carpeta que este archivo.

import constantes

precio = 100
total = precio + precio * constantes.IVA

print("IVA:", constantes.IVA)
print("Total:", total)
