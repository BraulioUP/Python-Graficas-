"""Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre 
tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido."""

def save_multiplication_table():
    n = int(input("Introduzca un número entero entre 1 y 10:"))
    if n < 1 or n > 10:
        print("El número debe estar entre 1 y 10")
        return
    with open(f"table-{n}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n*i}\n")
            
save_multiplication_table()
