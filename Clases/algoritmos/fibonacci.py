#Fibonacci:0,1,1,2,3,5,8,13,21

#----inicio----
pregunta_numero='ingrese un numero : '

#---mensaje error---
error_entrada='numero no valido'

#----entradas---
numero=None
while(numero==None):
    try:
        numero=int(input(pregunta_numero))
    except ValueError:
        print(error_entrada)
print(numero)

numeroAnterior=0
numeroActual=1

if(numero==1):
    print(numeroAnterior)
elif(numero==2):
    print(numeroActual)
else:
    for i  in range(2,numero +1):
        print(i)
        aux=numeroActual
        numeroActual=numeroAnterior+numeroActual
        numeroAnterior=aux
        print(numeroActual)
    print('salida',numeroActual)


 

