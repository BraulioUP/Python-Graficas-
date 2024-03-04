import pandas as pd
import matplotlib.pyplot as plt



def datos_provincia_porcentajes(ruta):
    datos = pd.read_excel(ruta, skiprows=5)
    
    print(datos.columns)
    
    totales_por_franjas = [
    pd.to_numeric(datos.iloc[:, 2], errors='coerce') + pd.to_numeric(datos.iloc[:, 3], errors='coerce'),
    pd.to_numeric(datos.iloc[:, 4], errors='coerce') + pd.to_numeric(datos.iloc[:, 5], errors='coerce'),
    pd.to_numeric(datos.iloc[:, 6], errors='coerce') + pd.to_numeric(datos.iloc[:, 7], errors='coerce'),
    pd.to_numeric(datos.iloc[:, 8], errors='coerce') + pd.to_numeric(datos.iloc[:, 9], errors='coerce')
]

    return [franja.dropna().values.tolist() for franja in totales_por_franjas]

def diagrama_caja(ruta):
    totales = datos_provincia_porcentajes(ruta)
    
    plt.figure(figsize=(10, 6))
    
    etqs = ["Menores de 25", "25 a 29", "30 a 44", "Mayores de 45"]
    
    plt.boxplot(totales, labels=etqs)
    plt.title('Desempleo por Franjas de Edad en España')
    plt.xlabel('Franjas de Edad')
    plt.ylabel('Cantidad de Desempleados')
    
    plt.show()

ruta_datos =  "data/Cap8/parosexoedadprov.xls"

diagrama_caja(ruta_datos)
