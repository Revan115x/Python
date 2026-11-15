"""4. Dado una lista, hacer un programa que indique si está ordenada o no."""


lista = [1,2,3,4,5,6,7,8,9]

ordenada = True
for i in range(len(lista)-1):

    if lista[i] > lista[i+1]:
        ordenada = False

if ordenada:
    print("La lista está ordenada")
else:
    print("La lista no está ordenada")