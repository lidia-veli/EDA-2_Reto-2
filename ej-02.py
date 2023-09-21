N = input()  # numero de elementos que va a tener la lista

lista = list( map(int, input().split()) )  # lista de elementos
minimo = abs(lista[0])  # el primer elemento de la lista va a ser el mínimo

for i in lista[1:]: # recorremos la lista del 2º en adelante (el 1º está reservado para el mínimo)
    if abs(i) < minimo: # si el número es menor que el 'minimo' en el momento
        minimo = abs(i)  # lo sustituimos

print(minimo)
