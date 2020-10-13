import random
import pandas as pd
SEPARADOR=("*" *20) + "\n"

diccionario_notas= {"Crecencio":[87,100,None], \
                    "Domitilia":[80,None,57], \
                    "Rutilio":[80,78,57],\
                    "Ludoviko":[100,100,100]}

notas_diccionario= pd.DataFrame(diccionario_notas)
print(notas_diccionario)

print(SEPARADOR)
#diccionario con comprension de listas
diccionario_notas_aleatorias= { \
    "Crecencio":[random.randrange(60,101) for x in range(3)],
    "Domitilia":[80,100,57], "Rutilio":[80,70,57] , "Panfilo":[20,100,100], \
    "Ludoviko":[100,100,100] }

notas_diccionarios = pd.DataFrame(diccionario_notas_aleatorias)
print(notas_diccionarios)

print(SEPARADOR)

notas_diccionario.index=["Programacion","Base De Datos", "Contabilidad"]
print(notas_diccionario)
print(SEPARADOR)


diccionario_notas= {"Crecencio":[87,100,None], \
                    "Domitilia":[80,None,57], \
                    "Rutilio":[80,78,57],\
                    "Ludoviko":[100,100,100]}


notas_diccionario= pd.DataFrame(diccionario_notas)
print(notas_diccionario)


