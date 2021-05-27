import time
tiempoInicial= time.time()
print('Holaa')
tiempoFinal= time.time()
delta=tiempoFinal-tiempoInicial
print(delta)

#-----inicio conteo---
tiempoInicial= time.time()

#-----instrucciones----
print('Hola a todos')
x=int(input('ingrese un numero x : '))
for i in range(x):
    print(i)
#-----cierre conteo----
tiempoFinal=time.time()
delta=tiempoFinal-tiempoInicial
print(delta)
