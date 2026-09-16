"""Realiza un programa que reciba una cantidad de minutos y muestre por
pantalla a cuantas horas y minutos corresponde."""

min=int(input("Minutos"))

horas= min // 60
minutos_R = min % 60

print(horas, "horas y", minutos_R, "minutos")