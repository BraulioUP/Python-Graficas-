# import libraries
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

s=Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=s)
driver.get('https://www.bolsasymercados.es/bme-exchange/es/Indices/Resumen')

time.sleep(10)  

tabla = driver.find_element(By.CSS_SELECTOR, 'table')

for fila in tabla.find_elements(By.TAG_NAME, "tr"):
    columnas = fila.find_elements(By.TAG_NAME, "td")
    if columnas:
        name = columnas[0].text
        price = columnas[2].text
        print("Indice:", name)
        print("Valor:", price)

driver.quit()   


"""
#Para Chrome:

from selenium import webdriver
w
from selenium.webdriver.common.by import By
import time


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get('https://www.bolsasymercados.es/bme-exchange/es/Indices/Resumen')

time.sleep(10)  # Espera a que se cargue la página



tabla = driver.find_element(By.CSS_SELECTOR, 'table')

for fila in tabla.find_elements(By.TAG_NAME, "tr"):
    columnas = fila.find_elements(By.TAG_NAME, "td")
    if columnas:
        name = columnas[0].text
        price = columnas[2].text
        print("Indice:", name)
        print("Valor:", price)

driver.quit()

"""