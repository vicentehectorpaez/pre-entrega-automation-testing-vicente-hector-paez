import pytest  # importamos pytest
from selenium import webdriver  # importamos el webdrivers de selenium
from selenium.webdriver.chrome.service import Service  # importamos los servicios de selenium a traves de la clase services
from webdriver_manager.chrome import ChromeDriverManager  # importamos el drivers correcto del navegador que vamos a utilizar 
from selenium.webdriver.common.by import By # clases common del webdriver pro medio del by


# configuramos un fixture para pasar servicios de instalacion correctos de los drivers correctos del navegador que vamos a utilizar 
@pytest.fixture(scope="module")
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

# test para validar si el titulo de la pagina es el correcto 
def test_02_verificar_inventario(driver):

    page_title = driver.title
    captura_texto_del_span = driver.find_element(By.CLASS_NAME, 'title').text  # asingo a una variable el valor del texto que tiene la etiqueta <span> en title en saucedemo 
   
    assert page_title == "Swag Labs" , F'ERROR: Titulo de la ventana "Swag Labs", obtenido {page_title}' # confirma si el titulo de la pagina es igual Swag Labs
    assert captura_texto_del_span == 'Products', f'ERROR: Titulo de la seccion esperado Products , Obtenido {captura_texto_del_span}' # verifica si el textContent de la etiqueta span es igual Products

def test_03_productos_visibles(driver):

    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    # el largo de la lista con len() para ver que tan largo es una lista  porque el inventory_item es similar a una lista 
    assert len(productos) > 0 , f'ERROR: No se encontraron items en la lista' # si la lista es mayor a 0 el test pasa almenos hay un elemento 

def test_04_nombre_precio_producto(driver):

    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item') 
    primer_producto = productos[0]

    nombre_producto = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_name')
    precio_producto = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_price')

    assert nombre_producto.text == 'Sauce Labs Backpack', f'ERROR: El nombre del producto no se encontro o no es el mismo a, {nombre_producto}'
    assert precio_producto.text == '$29.99', f'ERROR: El precio del producto no se encontro o no es le mismo a , {precio_producto}'

    
    




    



