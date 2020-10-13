import pandas as pd
import random



diccionario_notas= {"Crecencio":[87,100,None], \
                    "Domitilia":[80,None,57], \
                    "Rutilio":[80,78,57],\
                    "Ludoviko":[100,100,100]}


notas_diccionario= pd.DataFrame(diccionario_notas)
print(notas_diccionario)
print("")

notas_diccionario.index=["Programacion","Base De Datos", "Contabilidad"]
print(notas_diccionario)
print("")

print(notas_diccionario["Domitilia"])
print("")

print(notas_diccionario.Domitilia)

print("")


print(notas_diccionario.loc["Programacion"])
print()
print(notas_diccionario.loc["Base De Datos"])
print()
print(notas_diccionario.loc["Contabilidad"])





