"""
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla
de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe
debe mostrar un mensaje por pantalla informando de ello

"""

def mostrar_tabla_de_multiplicacion_linea():
    n = int(input("Ingrese un número entero entre 1 y 10: "))
    m = int(input("Ingrese un número entero entre 1 y 10: "))
    if n < 1 or n > 10 or m < 1 or m > 10:
        print("Los números deben estar entre 1 y 10")
        return
    try:
        with open(f"table-{n}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) >= m:
                print(lineas[m-1])
            else:
                print(f"El archivo table-{n}.txt no tiene {m} líneas.")
    except FileNotFoundError:
        print(f"El archivo table-{n}.txt no existe.")

mostrar_tabla_de_multiplicacion_linea()
