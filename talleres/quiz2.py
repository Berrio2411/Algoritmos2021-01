#Punto 1:Mostrar en pantalla la siguiente información haciendo uso de la librería pandas,
# referentes a los pacientes tratados en Medellín durante el año 2020
import pandas as pd
dicPacientesTratados = {}
dicPacientesTratados['Enero'] = 32121
dicPacientesTratados['Febrero'] = 14564
dicPacientesTratados['Marzo'] = 65465
dicPacientesTratados['Abril'] = 85202
dicPacientesTratados['Mayo']= 93213
dicPacientesTratados['Junio'] = 100231
dicPacientesTratados['Julio'] =120213
dicPacientesTratados['Agosto'] = 65421
dicPacientesTratados['Septiembre'] = 46546
dicPacientesTratados['Octubre']= 46547
dicPacientesTratados['Noviembre'] = 84651
dicPacientesTratados['Diciembre'] = 140521
seriesPacientesTratadosPorMes = pd.Series([32121,14564,65465,85202,93213,100231,120213,65421,46546,46547,84651,140521])
print (seriesPacientesTratadosPorMes)

#Punto 2 Mostrar en pantalla la información, pero dividida en cuatrimestres 
seriesPacientesPorCuatrimestre = pd.Series (dicPacientesTratados)
print (seriesPacientesPorCuatrimestre['Enero':'Abril'])
print (seriesPacientesPorCuatrimestre['Mayo':'Agosto'])
print (seriesPacientesPorCuatrimestre['Septiembre':'Diciembre'])

#Punto 3 Mostrar en pantalla el promedio de pacientes atendidos por mes en Medellín durante el 2020 
from functools import reduce
listaPacientesPorMes = [32121,14564,65465,85202,93213,100231,120213,65421,46546,46547,84651,140521]
sumar = lambda acumulado = 0, elemento = 0: acumulado + elemento
promediar = reduce (sumar, listaPacientesPorMes)/len (listaPacientesPorMes)
print (f'el promedio de pacientes atendidos es {promediar}')

#Punto 4 Mostrar en pantalla la siguiente información haciendo uso de la librería pandas,
# se sabe que las enfermedades en Bogotá estaban distribuidas así durante el primer
# semestre del 2020

matrizEnfermedadesDic = {
                        'Enfermedad General' :  [32121,14564,65465,85202,93213,100231],
                        'Covid 19' :  [0,0,223,3453,4543,43643],
                        'Traumatismo' :  [6545,43243,67657,435435,345345,43543],
                        'Cancer' :  [6541,4334,4323,34545,5454,7675],
}
dataFrameEnfermedades=pd.DataFrame(matrizEnfermedadesDic, index=['Enero','Febrero','Marzo','Abril','Mayo','Junio'] )
print(dataFrameEnfermedades)

#Punto 5 Mostrar en pantalla el promedio de pacientes por covid-19 durante los meses de
# abril, mayo, 

from functools import reduce
listaPacientesCovid = [3453,4543,43643]
sumar = lambda acumulado = 0, elemento = 0: acumulado + elemento
promediar2 = reduce (sumar, listaPacientesCovid)/len (listaPacientesCovid)
print (f'el promedio de pacientes con covid en los Meses Abril,Mayo y Junio es {promediar2}')

#Punto 6 Mostrar en pantalla la información de los primeros tres meses de pacientes tratados por traumatismos o cáncer
print(dataFrameEnfermedades[['Traumatismo','Cancer']]['Enero':'Marzo'])

#Punto 7  Cree una función Filter que dada la lista de pacientes con enfermedad general muestre aquellos datos que superen los 40000 pacientes.
listaPacientes=[32121,14564,65465,85202,93213,100231]
mayor=lambda elemento : elemento> 40000
listaMayor=list(filter(mayor,listaPacientes))
print(listaMayor)
#Punto 8 Utilizando la función Map multiplique por 10% todos los pacientes con cáncer y muestre en pantalla la lista obtenida
listaPacientesCancer=[6541,4334,4323,34545,5454,7675]
multiplo=0.1
multiplicador = lambda elemento : elemento * multiplo
listaCancer = list (map(multiplicador, listaPacientesCancer))
print (listaCancer)
#Punto 9  Utilizando la función reduce muestre en pantalla la suma de los pacientes que presentaron traumatismos

from functools import reduce
listaPacientesTraumatismo = [6545,43243,67657,435435,345345,43543]
sumar2 = lambda acumulado = 0, elemento = 0: acumulado + elemento
sumatoria = reduce (sumar, listaPacientesTraumatismo)
print (f'la sumatoria de los pacientes con traumatismo es {sumatoria}')
