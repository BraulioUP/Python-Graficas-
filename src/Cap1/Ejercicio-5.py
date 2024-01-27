"""
Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la 
Unión Europea (url:https://ec.europa.eu/eurostat/estat-navtree-portletprod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true), pregunte por las iniciales de 
un país y muestre el PIB per cápita de ese país de todos los años disponibles.

"""
import pandas as pd
import requests
from io import BytesIO
import gzip

def pib_per_capita_by_country(country_initials):
    url = "https://ec.europa.eu/eurostat/api/dissemination/"

    response = requests.get(url)

    if response.status_code == 200:
        compressed_file = BytesIO(response.content)

        with gzip.open(compressed_file, 'rt') as f:
            data = pd.read_csv(f, sep='\t')

            country_data = data[data['geo\\time'] == country_initials]

            if not country_data.empty:
                print(country_data)
            else:
                print(f"No hay datos disponibles para el país con iniciales {country_initials}")
    else:
        print("Error al obtener el archivo de datos")
country_initials = input("Ingrese las iniciales de un país: ")

pib_per_capita_by_country(country_initials)
