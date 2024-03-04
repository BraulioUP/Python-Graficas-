import pandas as pd
import matplotlib.pyplot as plt

ruta_datos = "data/Cap8/parosexoedadprov.xls"
datos = pd.read_excel(ruta_datos, skiprows=4)  

datos.columns = [
    'Unnamed: 0', 'Ciudad', 'Total Edad', 'Hombres Total', 'Mujeres Total',
    'Hombres <25', 'Mujeres <25', 'Hombres 25-29', 'Mujeres 25-29',
    'Hombres 30-44', 'Mujeres 30-44', 'Hombres >44', 'Mujeres >44'
]
datos = datos.drop(columns=['Unnamed: 0'])

ciudades = datos['Ciudad'].astype(str)
totales_hombres = datos['Hombres Total']
totales_mujeres = datos['Mujeres Total']

plt.figure(figsize=(10, 8)) 
bar_width = 0.35 

plt.bar(ciudades, totales_hombres, width=bar_width, label='Hombres', color='blue')

plt.bar(ciudades, totales_mujeres, width=bar_width, label='Mujeres', color='red', bottom=totales_hombres)

plt.xlabel('Ciudades')
plt.ylabel('Cantidad de personas')
plt.title('Cantidad de Hombres y Mujeres por Ciudad')
plt.xticks(rotation=90) 
plt.legend()

plt.tight_layout()
plt.show()