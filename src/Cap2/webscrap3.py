from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=s)

driver.get('https://www.inmuebles24.com/terrenos-en-venta-en-fraccionamiento-bugambilias.html')

WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-qa='posting PROPERTY']")))

anuncios = driver.find_elements(By.CSS_SELECTOR, "div[data-qa='posting PROPERTY']")

for anuncio in anuncios:
    try:
        descripcion = anuncio.find_element(By.CSS_SELECTOR, "div[data-qa='POSTING_CARD_DESCRIPTION']").text
        
        precio = anuncio.find_element(By.CSS_SELECTOR, "div[data-qa='POSTING_CARD_PRICE']").text
        
        ubicacion = anuncio.find_element(By.CSS_SELECTOR, "div[data-qa='POSTING_CARD_LOCATION']").text
        
        print("Descripción:", descripcion)
        print("Precio:", precio)
        print("Ubicación:", ubicacion)
        print("----------")
    except Exception as e:
        print("Error extrayendo datos de un anuncio:", e)

driver.quit() 