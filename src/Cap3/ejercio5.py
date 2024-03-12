import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_evolucion_ventas(ventas, tipo):
    '''Función que construye un diagrama del tipo indicado con la evolución de las ventas por años.
    
    Parámetros:
        - ventas: Es un dataframe de Pandas con las ventas, siendo el índice los años.
        - tipo: Es una cadena con el tipo de gráfico a dibujar: lineas, barras, sectores o areas.

    Salida:
        Un gráfico del tipo indicado con la evolución de las ventas.
    '''
    # Definimos un diccionario con los tipos de gráficos
    graficos = {'lineas':'line', 'barras':'bar', 'sectores':'pie', 'area':'area'}
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos las series de líneas con los ingresos y los gastos
    ventas.plot(kind = graficos[tipo], ax = ax)
    # Añadimos el título
    plt.title('Evolución del número de ventas')
    # Devolvemos el objeto con los ejes y el gráfico que contienten
    return ax

df_ventas = pd.Series([1200, 840, 1325, 1280, 1500], index = [2000, 2001, 2002, 2003, 2004])
diagrama_evolucion_ventas(df_ventas, 'lineas')
plt.show()
diagrama_evolucion_ventas(df_ventas, 'area')
plt.show()
diagrama_evolucion_ventas(df_ventas, 'barras')
plt.show()
diagrama_evolucion_ventas(df_ventas, 'sectores')
plt.show()