from xlrd import open_workbook, colname
import xlwt

ruta = 'data/Cap1/subvenciones.xls'
ruta1 = 'data/Cap1/subvenciones_esc.csv'

with open_workbook(ruta,on_demand=True) as libro:
    asociaciones = {}
    for nombre in libro.sheet_names():
        hoja = libro.sheet_by_name(nombre)
        for i in range(1,hoja.nrows):
            fila = hoja.row(i)
            centro = fila[0].value
            subvencion = fila[2].value
            #print(fila[0].ctype)
            #print(fila[2].value)
            if centro in asociaciones:
                asociaciones[centro] = asociaciones[centro] + subvencion
            else:
                asociaciones[centro] = subvencion
    print(asociaciones)