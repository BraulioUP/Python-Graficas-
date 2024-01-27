"""
Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los 
clientes de una empresa. El programa incorporar funciones crear el fichero con el listín si no existe, 
para consultar el teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el 
teléfono de un cliente. El listín debe estar guardado en el fichero de texto listin.txt donde el 
nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea 
distinta

"""

def create_phonebook_file_if_not_exists():
    try:
        with open("listin.txt", "x"):
            pass
    except FileExistsError:
        pass

def find_phone_number(name):
    with open("listin.txt", "r") as file:
        for line in file:
            entry = line.strip().split(",")
            if entry[0] == name:
                return entry[1]
    return f"No phone number found for {name}"

def add_phone_number(name, phone_number):
    with open("listin.txt", "a") as file:
        file.write(f"{name},{phone_number}\n")

def delete_phone_number(name):
    with open("listin.txt", "r") as file:
        lines = file.readlines()
    with open("listin.txt", "w") as file:
        for line in lines:
            entry = line.strip().split(",")
            if entry[0] != name:
                file.write(line)

# Usage
create_phonebook_file_if_not_exists()
print(find_phone_number("John"))
add_phone_number("Jane", "123456789")
delete_phone_number("John")
