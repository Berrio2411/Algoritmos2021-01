from functools import reduce
lista = [12,14,7,21,49,23,45,46,574,32,54]
multiplicador = lambda acumulado = 0, elemento = 1: acumulado * elemento
multiplicado = reduce (multiplicador, lista)/len (lista)
print (multiplicado)