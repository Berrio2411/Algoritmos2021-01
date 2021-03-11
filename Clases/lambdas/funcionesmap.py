lista=[2,25,34,65]
potenciador= lambda valor=0 : valor**2
print(potenciador(4))
listaCuadrados= list(map(potenciador,lista))
print(listaCuadrados)

n=int(input('Ingrese valor a restar: '))
restarN= lambda valor : valor - n

print(restarN(3))
restarNlista= list(map(restarN,lista))
print(restarNlista)


#normalizar
mayor= max(lista)
dividir= lambda valor=0 : round(valor/mayor,2)
listaNormalizada=list(map(dividir,lista))
print(listaNormalizada)
 ##IMC
pesos=[]
estaturas=[]
imc=lambda peso=0 , altura=1: peso / altura**2
imcListas=list(map(imc,pesos,estaturas))
print(imcListas)

## Area triangulo
bases=[2,34,2,5,345]
alturas=[23,345,6,67,23]
divisores=[2,2,2,2,2]

calcularAreaTriangulo= lambda base=0,altura=0,divisores=1: base*altura/divisores
listaAreasTriangulo=list(map(calcularAreaTriangulo,bases,alturas,divisores))

