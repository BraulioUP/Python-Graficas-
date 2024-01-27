"""
Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el
número de palabras que contiene.

"""


import requests

def count_words_in_file(url):
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        words = content.split()
        num_words = len(words)
        print(f"El archivo de {url} contiene {num_words} palabras."
)
    else:
        print(f"No se pudo recuperar el archivo de {url}"
)

# Usage
url = "https://teams.microsoft.com/v2/"
count_words_in_file(url)