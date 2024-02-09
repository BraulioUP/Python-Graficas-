
"""
Web scraping a una la hora y fecha en mexico
https://hora.mx/Mexico?classId=73b2d613-0432-433f-8ce2-0c9772c7ded6&assignmentId=6e4f4bf0-a244-47be-98c9-1a4dfaffa54b&classId=da61f51a-fef6-48b0-8760-776aa28bf809&assignmentId=615cb8e4-bc30-4e29-ad17-ecc18433f7ed&submissionId=aa8b4167-222a-4fec-b09f-44f5f5d631bc
"""

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def main():
    webdriver_service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=webdriver_service)

    driver.get('https://hora.mx/Mexico')

    driver.implicitly_wait(10)

    hora = driver.execute_script("return document.querySelector('.p_h').textContent;")
    fecha = driver.execute_script("return document.querySelector('.p_d').textContent;")

    print(f'La hora actual en México es: {hora}')
    print(f'La fecha actual en México es: {fecha}')

    driver.quit()


if __name__ == "__main__":  
    main()