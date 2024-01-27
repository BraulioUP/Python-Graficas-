"""
Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla 
de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el 
fichero no existe debe mostrar un mensaje por pantalla informando de ello.

"""

def show_multiplication_table():
    n = int(input("Introduzca un número entero entre 1 y 10: "))
    if n < 1 or n > 10:
        print("El número debe estar entre 1 y 10")
        return
    try:
        with open(f"table-{n}.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"El archivo table-{n}.txt no existe.")
        
show_multiplication_table()