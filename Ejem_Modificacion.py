SEPARADOR=("*" *20) + "\n"
import pandas as pd  
impopandas as pd 

diccionario_notas_aleatorias= { \
    "Crecencio":[random.randrange(60,101) for x in range(3)],
    "Domitilia":[80,100,57], "Rutilio":[80,70,57] , "Panfilo":[20,100,100], \
    "Ludoviko":[100,100,100] }

notas_diccionarios = pd.DataFrame(diccionario_notas_aleatorias)
notas_diccionarios.index = ["Programacion" , "Base de datos" , "Contabilidad"]

print("Todas las asignaturas , todos los estudiantes")
subConjunto = notas_diccionarios.loc["Programacion":"Contabilidad"]
print(subConjunto)
print(SEPARADOR)

print("Ultimas dos asignaturas, todos los estudiantes")
subConjunto= notas_diccionarios.loc["Base de datos": "Contabilidad"]
print(subConjunto)
print(SEPARADOR)

print("SubConjunto , solamente las notas de Rutilio y Ludoviko")
subConjunto= notas_diccionarios.loc["Programacion":"Base de datos" , ["Rutilio" , "Ludoviko"]]
print(subConjunto)
print(SEPARADOR)

print("Solamente calificaciones aprobatorias")
aprobados= notas_diccionarios[notas_diccionarios >=70]
print(aprobados)
print(SEPARADOR)

print("Solamente calificaciones aprobatorias entre 70 y 80")
aprobados = notas_diccionarios[(notas_diccionarios >=70) & (notas_diccionarios <=80)]
print(aprobados)
print(SEPARADOR)

print("Solamente calificaciones  NO aprobatorias y que sean pares")
reprobadas_pares=notas_diccionarios[(notas_diccionarios <70) & (notas_diccionarios %2 == 0)]
print(reprobadas_pares)
print(SEPARADOR)

print("La calificacion de Panfilo en Programacion")
calif_panfilo_progra = notas_diccionarios.at["Programacion","Panfilo"]
print(calif_panfilo_progra)
print(SEPARADOR)

print("Modificamos la calif de Pnafilo en Programacion")
notas_diccionarios.at["Programacion", "Panfilo"] = 100
calif_modif_panfilo= notas_diccionarios.at["Programacion","Panfilo"]
print(calif_modif_panfilo)
print(SEPARADOR)
