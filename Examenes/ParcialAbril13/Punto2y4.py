#Punto 4 :
'Se mediran los tiempos de ambas funciones y se determinara cual es más rapida'

import contarPalabras_2 as p2
import contarPalabras_1 as p1
import time

parrafo= '''La justicia sobre la fuerza es la impotencia, la fuerza sin justicia es tiranía.
              Vale más saber alguna cosa de todo que saberlo todo de una sola cosa.
              Dos excesos: excluir la razón, no admitir más que la razón.
              Nuestra naturaleza está en movimiento. El reposo absoluto es la muerte.
              El hombre tiene ilusiones como el pájaro alas. Eso es lo que lo sostiene.
              El hombre está dispuesto siempre a negar todo aquello que no comprende.
              Aquel que duda y no investiga, se torna no sólo infeliz, sino también injusto.
              A fuerza de hablar de amor, uno llega a enamorarse.
              ¿De qué le sirve al hombre ganar el mundo si pierde su alma?'''

inicio= time.time()
p1=parrafo
deltap1=time.time()-inicio

inicio= time.time()
p2=parrafo
deltap2=time.time()-inicio

print(deltap1,deltap2)

#Analisis= Despúes de hacer varias en la que los tiempo eran 0.0 
# se pudo ver que el algoritmo numero 2 (p2) es un poco más rapido 
# y tiene sentido ya que al analizar un poco ambos nos encontramos
# que  el algoritmo 2 no repite el conteo de cada una de las palabras
# cosa que si  hace el algoritmo 1


#Punto 2
#Formula del codigo: 8+XYW+X+W
