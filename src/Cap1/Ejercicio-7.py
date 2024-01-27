"""
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes 
columnas: Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo
(precio máximo de la acción durante la jornada), Mínimo (precio mínimo de la acción durante la 
jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de
euros).
1. Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los 
datos del fichero por columnas.
2. Construir una función que reciba el diccionario devuelto por la función anterior y cree un 
fichero en formato csv con el mínimo, el máximo y la media de dada columna
"""

import pandas as pd

def read_stock_data(file_path):
    stock_data = pd.read_csv(file_path)
    stock_dict = stock_data.to_dict(orient='list')
    return stock_dict

def create_summary_csv(stock_dict, output_file):
    summary_data = {
        'Minimum': [],
        'Maximum': [],
        'Mean': []
    }
    for column, values in stock_dict.items():
        summary_data['Minimum'].append(min(values))
        summary_data['Maximum'].append(max(values))
        summary_data['Mean'].append(sum(values) / len(values))
    
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv(output_file, index=False)

file_path = "data/Cap1/cotizacion.csv"
stock_data_dict = read_stock_data(file_path)
print(stock_data_dict)  
create_summary_csv(stock_data_dict, "stock_summary.csv")
print("Archivo stock_summary.csv creado con el resumen de cotizaciones") 