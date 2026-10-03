import pytest  # importamos pytest
from selenium import webdriver  # importamos el webdrivers de selenium
from selenium.webdriver.chrome.service import Service  # importamos los servicios de selenium a traves de la clase services
from webdriver_manager.chrome import ChromeDriverManager  # importamos el drivers correcto del navegador que vamos a utilizar 
from selenium.webdriver.common.by import By # clases common del webdriver pro medio del by


# configuramos un fixture para pasar servicios de instalacion correctos de los drivers correctos del navegador que vamos a utilizar 
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    yield driver  

    driver.quit()

# test para validar login 
def test_01_login(driver):
    driver.get("https://www.saucedemo.com/") #con get accede a la pagina y abre el navegador con la url 

    driver.find_element(By.ID, "user-name").send_keys("standard_user") #encuentra con metodo find_element mediante un selector en este caso ID el username
    driver.find_element(By.ID, "password").send_keys("secret_sauce") #encuentra con metodo find_element mediante un selector en este caso ID el password
    driver.find_element(By.ID, "login-button").click() #encuentra con metodo find_element mediante un selector en este caso el evento click del boton 

    assert "/inventory.html" in driver.current_url, "ERROR: No se reidirigio a la pagina /inventory.html" # lo que hace es confirmar si /invetory.html si se encuentra en esta url https://www.saucedemo.com/ el test pasa ? 


    



