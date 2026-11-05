"""5. Escribir dos funciones que permitan calcular:
• La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
• La cantidad de horas, minutos y segundos de un tiempo dado en segundos."""

horas = int(input("DIME UNA CANTIDAD DE HORAS: "))

minutos = int(input("DIME UNA CANTIDAD DE MINUTOS: "))

segundos = int(input("DIME UNA CANTIDAD DE SEGUNDOS: "))

def calcularS (horas,minutos,segundos):

    horaseg=( 60*60 ) * horas
    mins=minutos*60

    resultado = horaseg + mins + segundos;

    return resultado

print("PASAMOS DE HORAS A SEGUNTOS")
print(calcularS(horas,minutos,segundos))

segundos = int(input("DIME UNA CANTIDAD DE SEGUNDOS: "))

def calcularH(segundos):

    horas = segundos // (60 * 60)

    resto = segundos % 3600

    minutos = resto // 60

    segundos_restantes = resto % 60

    resultado = str(horas) + " H " + str(minutos) + " Min " + str(segundos_restantes) + " Seg"

    return resultado

print("PASAMOS DE SEGUNDOS A HORAS")
print(calcularH(segundos))