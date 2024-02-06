import requests
from bs4 import BeautifulSoup

url = "https://www.marcadores.com/futbol/mexico/liga-mexicana/?classId=73b2d613-0432-433f-8ce2-0c9772c7ded6&assignmentId=3395aeb5-729d-4595-acea-3dd15f6a2c5e&classId=57dd230f-55db-4a8b-a4b8-42a51d1034fa&assignmentId=d7187cc3-bfef-43a1-8c60-8afdcbd07200&classId=da61f51a-fef6-48b0-8760-776aa28bf809&assignmentId=41d5500b-2926-4834-b0bf-c5dbabd9c941&submissionId=a81c8883-8048-dd0f-cd9d-b6565d6dc3a5"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find('table', {'class': 'table matches table-condensed layout-fixed'})


rows = table.find_all('tr', {'data-link': True})


for row in rows:
    date = row.find_previous_sibling('tr', {'class': 'league-data'}).find('th').text.strip()
    time = row.find('span', {'class': 'hour'}).text.strip()
    home_team = row.find('span', {'class': 'team1'}).text.strip()
    away_team = row.find('span', {'class': 'team2'}).text.strip()
    score = row.find('span', {'class': 'score'}).text.strip()
    print(f"Fecha: {date}, Hora: {time}, Equipos: {home_team} vs {away_team}, Marcador: {score}")