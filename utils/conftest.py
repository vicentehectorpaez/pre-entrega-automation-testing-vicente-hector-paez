import pytest  # importamos pytest
from selenium import webdriver  # importamos el webdrivers de selenium
from selenium.webdriver.chrome.service import Service  # importamos los servicios de selenium a traves de la clase services
from webdriver_manager.chrome import ChromeDriverManager  # importamos el drivers correcto del navegador que vamos a utilizar 

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    yield driver  

    driver.quit()
