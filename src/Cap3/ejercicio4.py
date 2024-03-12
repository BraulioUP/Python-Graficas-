"""
Escribir una función que reciba una serie de Pandas con el número de ventas de un 
producto durante los meses de un trimestre y un título y cree un diagrama de sectores con 
las ventas en formato png con el título dado. El diagrama debe guardarse en un fichero con 
formato png y el título dado

"""


import matplotlib.pyplot as plt
import pandas as pd

def crear_diagrama(ventas, titulo):
    # Crear el diagrama de sectores
    plt.pie(ventas, labels = ventas.index, autopct='%1.1f%%')
    plt.title(titulo)
    
    # Guardar el diagrama en un archivo png
    plt.savefig(f"{titulo}.png")
    plt.close()
    
    

ventas = pd.Series([100, 200, 150], index=['Enero', 'Febrero', 'Marzo'])
crear_diagrama(ventas, 'Ventas del primer trimestre')