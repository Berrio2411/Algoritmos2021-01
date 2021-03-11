def linedesing (cantidad=60):
    print('#'*cantidad)

def sumar(a,b):
    suma= a+b
    return suma

def restar(a,b):
    resta= a-b
    return resta

def multiplicar(a,b):
    multiplicacion= a*b
    return multiplicacion

def dividir(a,b):
    division= a/b
    return division

def calculadora(funcion,a,b):
    return funcion (a,b)




linedesing(30)
print('Hola a todos')
linedesing(20)
print(sumar(2,6))

linedesingLambda= lambda cantidad=60: print('#'*cantidad)
linedesingLambda ()

sumarl= lambda a=0 ,b=0: a+b
print(sumarl(2,7))








listaEdades=[34,12,18,14,22,17]
listaEdades2=[45,23,27,19,20,23] 
lambdaMaximo= lambda x=[], y=[] : print(max(x),max(y))
lambdaMaximo(listaEdades,listaEdades2)

mayorEdad= lambda edad=0 : edad>=18
print(mayorEdad(14))
print(mayorEdad(19))
mayores= list(filter(mayorEdad,listaEdades))
print(mayores)

