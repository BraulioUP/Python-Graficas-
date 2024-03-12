import pandas as pd 
import matplotlib.pyplot as plt 

def diagrama_lineas_ingresos_gastos(datos):
    '''Función que construye un diagrama de lineas con los ingresos y gastos de un cuatrimestre.
    
    Parámetros:
        - datos: Es un dataframe de Pandas con dos columnas, una para los ingresos y otra para los gastos, y como índice los meses.

    Salida:
        Un gráfico de líneas con los ingresos y los gastos dados.
    '''
    # Definimos la figura y los ejes del gráfico con Matplotlib
    fig, ax = plt.subplots()
    # Dibujamos las series de líneas con los ingresos y los gastos
    datos.plot(ax = ax)
    # Añadimos la escala del eje y
    ax.set_ylim([0, max(datos.Ingresos.max(), datos.Gastos.max()) + 500])
    # Añadimos el título
    plt.title('Evolución de ingresos y gastos')
    # Devolvemos el objeto con los ejes y el gráfico que contienten
    return ax

datos = {'Mes':['Ene', 'Feb', 'Mar', 'Abr'], 'Ingresos':[4500, 5200, 4800, 5300], 'Gastos':[2300, 2450, 2000, 2200]}
df_datos = pd.DataFrame(datos).set_index('Mes')
diagrama_lineas_ingresos_gastos(df_datos)
plt.show()