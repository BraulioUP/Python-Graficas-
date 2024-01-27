"""
El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron 
dos exámenes parciales de teoría y un examen de prácticas. Los alumnos que tuvieron menos de 4 
en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria). 
Escribir un programa que contenga las siguientes funciones:
1. Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, 
donde cada diccionario contiene la información de los exámenes y la asistencia de un 
alumno. La lista tiene que estar ordenada por apellidos.
2. Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial 
de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de 
un 40%.
3. Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. 
Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los 
exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.

"""
import csv

# Función para leer el fichero de calificaciones y devolver una lista de diccionarios ordenada por apellidos
def leer_calificaciones(filename):
    calificaciones = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            calificaciones.append(row)
    return calificaciones

# Función para calcular la nota final de cada alumno y añadirla al diccionario
def calcular_nota_final(calificaciones):
    for alumno in calificaciones:
        # Convertir las calificaciones de texto a números
        parcial1 = float(alumno['Parcial1'].replace(',', '.'))
        parcial2 = float(alumno['Parcial2'].replace(',', '.'))
        practicas = float(alumno['Practicas'].replace(',', '.'))
        asistencia = float(alumno['Asistencia'].strip('%'))  # Eliminar el símbolo de porcentaje y convertir a float
        
        # Calcular la nota final con los pesos dados
        nota_final = (parcial1 + parcial2) / 2 * 0.3 + practicas * 0.4
        alumno['Nota_Final'] = nota_final

# Función para separar los alumnos aprobados de los suspendidos
def separar_aprobados_suspensos(calificaciones):
    aprobados = []
    suspendidos = []
    for alumno in calificaciones:
        # Verificar las condiciones para aprobar el curso
        if (float(alumno['Asistencia'].strip('%')) >= 75 and
            float(alumno['Parcial1'].replace(',', '.')) >= 4 and
            float(alumno['Parcial2'].replace(',', '.')) >= 4 and
            float(alumno['Practicas'].replace(',', '.')) >= 4 and
            float(alumno['Nota_Final']) >= 5):
            aprobados.append(alumno)
        else:
            suspendidos.append(alumno)
    return aprobados, suspendidos

# Ejemplo de uso
filename = 'data/Cap1/calificaciones.csv'

# Paso 1: Leer el fichero de calificaciones
calificaciones = leer_calificaciones(filename)

# Paso 2: Calcular la nota final de cada alumno
calcular_nota_final(calificaciones)

# Paso 3: Separar aprobados y suspendidos
aprobados, suspendidos = separar_aprobados_suspensos(calificaciones)

# Imprimir resultados
print("Alumnos Aprobados:")
for alumno in aprobados:
    print(alumno)

print("\nAlumnos Suspensos:")
for alumno in suspendidos:
    print(alumno)

