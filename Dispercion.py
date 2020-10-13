import random
import pandas as pd
SEPARADOR=("*" *20) + "\n"



diccionario_notas_aleatorias= { \
    "Crecencio":[random.randrange(60,101) for x in range(3)],
    "Domitilia":[80,100,57], "Rutilio":[80,70,57] , "Panfilo":[20,100,100], \
    "Ludoviko":[100,100,100] }

notas_diccionarios = pd.DataFrame(diccionario_notas_aleatorias)
notas_diccionarios.index = ["Programacion" , "Base de datos" , "Contabilidad"]
#Medidas de dispercion
print(notas_diccionarios.describe())
print(SEPARADOR)

#media
print(notas_diccionarios.mean())
print(SEPARADOR)
print(notas_diccionarios.T)
print(SEPARADOR)

print(notas_diccionarios.T.describe())
print(SEPARADOR)
print(notas_diccionarios.T.mean())
print(SEPARADOR)
print(notas_diccionarios.T.std())
print(SEPARADOR)

print("Ordenar datos en un DataFrame")
print(notas_diccionarios.T.sort_values(by="Programacion"))
print(SEPARADOR)

print(notas_diccionarios.loc["Programacion"].sort_values())
print(SEPARADOR)












