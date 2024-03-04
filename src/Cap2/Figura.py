import matplotlib.pyplot as plt
import pandas as pd

ruta_datos= "data/Cap8/parosexoedadprov.xls"

def calcula_estadisticas(ciudad, ruta, mujeres=True):
    # Aquí debes definir la lógica de tu función
    return ([2435.0, 3744.0, 12567.0, 13774.0], ['MENORES DE 25 AÑOS', 'DE 25 A 29 AÑOS','DE 30 A 44 AÑOS','MAYORES DE 45 AÑOS'])
    

def paro_edades_tarta(ciudad, ruta, mujeres=True):
   vals, etqs = calcula_estadisticas(ciudad, ruta, mujeres)
   fig, ejes = plt.subplots()
   explode = (0, 0, 0, 0.1)
   cunhas, text_cat, text_porc = ejes.pie(vals, explode=explode, labels=etqs, autopct='%1.1f%%', shadow=True, startangle=90)
   ejes.axis('equal')
   plt.legend(cunhas, etqs, loc="best")
   plt.show()

paro_edades_tarta("ALMERIA", ruta_datos)

