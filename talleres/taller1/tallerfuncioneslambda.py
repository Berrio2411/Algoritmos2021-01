#Que devuelva el exponte n de un número dado
potenciador=lambda base=0 , exponente=0 : base**exponente
print(potenciador(5,4))

#Muestre en pantalla n veces un string ingresado
mostrarPalabra= lambda palabra,cantidad=0 :palabra*cantidad
print(mostrarPalabra('hola \n',15))

# Muestre en pantalla el máximo número de dos listas ingresadas
maximos= lambda lista1,lista2:print(max(lista1),max(lista2))
listaA=[34,25,33,28,22,19,45,32,18,44,35]
listaB=[23,12,37,44,29,32,24,56,35,27,18]
print(maximos(listaA,listaB))
#	Devuelva verdadero o falso dependiendo si un número es par o no
numeropar=lambda valor:valor%2==0
print(numeropar(6))
print(numeropar(3))
# Que devuelva la unión de dos palabras
unirPalabras= lambda palabra1,palabra2: palabra1 + ' ' +palabra2
print(unirPalabras('Hola','Santiago'))
#Que dado un nombre salude a la persona ingresada
ingresaNombre= 'ingrese su nombre por favor : '
nombre= input(ingresaNombre)
saludar= lambda name='': print(f'hola {name} bienvenido')
saludar(nombre)
# Que dada una palabra devuelva el largo de la misma
preguntaPalabra= 'ingrese una palabra por favor : '
palabraDada=input(preguntaPalabra)
lenPalabra= lambda palabra: len(palabra)
print(lenPalabra(palabraDada))
#Que utilizando la anterior muestre en pantalla el resultado
morstarLen= lambda funcion,palabra:print(funcion(palabra))
morstarLen(lenPalabra,palabraDada)
# Devuelva el área de un triángulo dada su base y altura
areaTriangulo = lambda base, altura : base*altura/2
area = areaTriangulo (7,8)
print (area)
#Calcule el imc sabiendo la altura y el peso (imc = peso / altura^2)
imcCalculator = lambda peso, altura : peso/(altura**2)
imc= imcCalculator(65,1.78)
print (imc)

