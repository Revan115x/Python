"""2. Escribe un programa que pida un número entero entre uno y doce e imprima el
número de días que tiene el mes correspondiente. Debes validar que el mes
introducido es correcto, en caso contrario lo indicas y lo pides de nuevo."""

mes = int(input("Introduce un número del 1 al 12: "))

while mes < 1 or mes > 12:
    print("Mes incorrecto")
    mes = int(input("Introduce un número del 1 al 12: "))

dia = int(input("Introduce un numero de dias: "))

if mes ==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    dias=31
elif mes==4 or mes==6 or mes==9 or mes==11:
    dias=30
elif mes==2 :
    dias=28
else:
    print("ERROR")

print(dias)