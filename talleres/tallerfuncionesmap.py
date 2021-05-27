#Crear una función map que haga lo siguiente:
#  Devuelva el cuadrado de cada elemento de la lista
potenciador = lambda valor : valor ** 2
lista = [8,4,23,42,15,33,21]
listaCuadrados = list (map(potenciador, lista))
print (listaCuadrados)

#• Divida a todos los elementos de la lista por el mayor número de la misma
lista2 = [4,8,9,13,25,43,29]
maximo = max (lista2)
normalizador = lambda valor : valor / maximo
listaNormalizada = list (map(normalizador, lista2))
print (listaNormalizada)

#Le reste un número n a la lista
lista3 = [2,5,6,12,25,43,21]
valor_n = 2
restador = lambda elemento : elemento  - valor_n

listaRestada = list (map(restador, lista3))
print (listaRestada)

# Le sume un número n a la lista

lista4 = [2,5,6,12,25,43,22]
valor_n = 2
sumador = lambda elemento : elemento  + valor_n

listaSumada = list (map(sumador, lista4))
print (listaSumada)

#Todos los elementos multiplicados * 5
lista5 = [2,5,6,12,25,33,21]
multiplo = 5
multiplicador = lambda elemento : elemento * multiplo

listaRestada = list (map(multiplicador, lista5))
print (listaRestada)
