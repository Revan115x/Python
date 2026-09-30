"""Supongamos que en un cajero automático queremos cargar una comisión
mínima de 10€ por cualquier cantidad retirada inferior a 1000€ y 10€ más por
cada unidad o fracción de 1000€ adicional (aclarando este galimatías bancario:
cobramos 10€ por retiradas de 0 a 999€, 20€ por retiradas de 1000 a 1999€,
30€ por retiradas de 2000 a 2999€, y así sucesivamente)."""

dineroBanco=5000
comision=0


print("CUENTA BANCO : ",dineroBanco)

retirar=float(input("Cantidad a Retirar "))

if retirar > 0 and retirar < 1000:
    dineroBanco = dineroBanco - retirar
    comision=10
elif retirar >=1000 and retirar < 2000:
    dineroBanco = dineroBanco - retirar
    comision=20
elif retirar >=2000 and retirar < 3000:
    dineroBanco = dineroBanco - retirar
    comision=30

print("SIN COMISION ",dineroBanco)
print("SE TE COBRARA LA COMISION DE UN ",comision,"%")
print(dineroBanco-comision)