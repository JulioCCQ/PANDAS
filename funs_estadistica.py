from pandas import *
SEPARADOR=("*" *20) + "\n"

notas = pd.Series([87,100,85,60,78])
print(type(notas))
print(notas)
print(SEPARADOR)

iguales = pd.Series(200, range(6))
print(type(iguales))
print(iguales)
print(SEPARADOR)

print("Notas: ")
print(f"{notas}")
print(f"Cantidad = {notas.count()}")
print(f"media = {notas.mean()} ")
print(f"minimo = {notas.min()} ")
print(f"maximo = {notas.max()} ")
print(f"Desviacion standar = {notas.std()}")
print("Sumarizacion descriptiva: ")
print(notas.describe())
print(SEPARADOR)
#con indices
print("Series con indices personalizados: ")
notas_asignadas= pd.Series([87,100,85,60,78],\
                           index=["Crecencio","Domitilia","Rutilia",\
                                  "Panfilo","Ludoviko"])
print(notas_asignadas)
print(SEPARADOR)
##con diccionario
print("Serie apartir de un diccionario: ")
notas_asignadas_dict= pd.Series({"Crecencio":87, "Domitilia":100, "Rutilia":85, \
                                  "Panfilo":60 ,"Ludoviko":78})
print(notas_asignadas_dict)

print(SEPARADOR)

print(f"La calificacion de Rutilia es {notas_asignadas_dict['Rutilia']}")
print(f"La calificacion de Rutilia es {notas_asignadas_dict.Rutilia}")
              









