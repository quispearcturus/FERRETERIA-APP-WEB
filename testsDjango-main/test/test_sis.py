import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Inicializa el driver de Chrome
    driver = webdriver.Chrome()
    yield driver
    # Cierra el driver al finalizar
    driver.quit()

def test_selenium_example(driver):
    # Navega a la URL
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    driver.set_window_size(789, 816)

    # Simula el inicio de sesión
    username_field = driver.find_element(By.ID, "id_username")
    username_field.send_keys("admin")
    username_field.send_keys(Keys.ENTER)

    # Espera a que el elemento con el texto "Personas" esté presente
    wait = WebDriverWait(driver, 10)  # Puedes ajustar el tiempo límite según tus necesidades
    element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Personas")))
    element.click()

    # Continúa con las acciones Selenium que desees probar
    driver.find_element(By.CSS_SELECTOR, "li > .addlink").click()
    driver.find_element(By.ID, "id_nombre").click()
    driver.find_element(By.ID, "id_nombre").send_keys("Juan")
    driver.find_element(By.ID, "id_apellido_paterno").click()
    driver.find_element(By.ID, "id_apellido_paterno").send_keys("Lopez")
    driver.find_element(By.ID, "id_apellido_materno").click()
    driver.find_element(By.ID, "id_apellido_materno").send_keys("Apaza")
    driver.find_element(By.NAME, "_save").click()
    driver.find_element(By.CSS_SELECTOR, "button:nth-child(2)").click()
