#import pytest  # importamos pytest
#from selenium import webdriver  # importamos el webdrivers de selenium
#from selenium.webdriver.chrome.service import Service  # importamos los servicios de selenium a traves de la clase services
#from webdriver_manager.chrome import ChromeDriverManager  # importamos el drivers correcto del navegador que vamos a utilizar 
from selenium.webdriver.common.by import By # clases common del webdriver pro medio del by
from utils.helpers import login





# configuramos un fixture para pasar servicios de instalacion correctos de los drivers correctos del navegador que vamos a utilizar 
#@pytest.fixture(scope="module")
#def driver():
#    service = Service(ChromeDriverManager().install())
#    driver = webdriver.Chrome(service=service)

#    yield driver  

#    driver.quit()

# test para validar login 
#def test_01_login(driver):
#    driver.get("https://www.saucedemo.com/") #con get accede a la pagina y abre el navegador con la url 

#   driver.find_element(By.ID, "user-name").send_keys("standard_user") #encuentra con metodo find_element mediante un selector en este caso ID el username
#   driver.find_element(By.ID, "password").send_keys("secret_sauce") #encuentra con metodo find_element mediante un selector en este caso ID el password
#   driver.find_element(By.ID, "login-button").click() #encuentra con metodo find_element mediante un selector en este caso el evento click del boton 

#funcion que llama al helper login y luego verifica si esta dentro de la pagina /inventory.html
def test_01_login(driver):  
    login(driver)  
    assert "/inventory.html" in driver.current_url, "ERROR: No se reidirigio a la pagina /inventory.html" # lo que hace es confirmar si /invetory.html si se encuentra en esta url https://www.saucedemo.com/ el test pasa ? 



# test para validar si el titulo de la pagina es el correcto 
def test_02_verificar_inventario(driver):
    
    page_title = driver.title
    captura_texto_del_span = driver.find_element(By.CLASS_NAME, 'title').text  # asingo a una variable el valor del texto que tiene la etiqueta <span> en title en saucedemo 
   
    assert page_title == "Swag Labs" , F'ERROR: Titulo de la ventana "Swag Labs", obtenido {page_title}' # confirma si el titulo de la pagina es igual Swag Labs
    assert captura_texto_del_span == 'Products', f'ERROR: Titulo de la seccion esperado Products , Obtenido {captura_texto_del_span}' # verifica si el textContent de la etiqueta span es igual Products



# test para validar si hay productos visibles 
def test_03_productos_visibles(driver):

    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    # el largo de la lista con len() para ver que tan largo es una lista  porque el inventory_item es similar a una lista 
    assert len(productos) > 0 , f'ERROR: No se encontraron items en la lista' # si la lista es mayor a 0 el test pasa almenos hay un elemento 



# test para validar el nombre y el precio del primer prodcucto del sitio 
def test_04_nombre_precio_producto(driver):

    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')     # busco todos los elemnentos de la lista y asigno a la variable producto 
    primer_producto = productos[0]     # asigno el primero producto de la lista a la variable primer_producto 

    nombre_producto = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_name')  # asigno a la variable nombre_producto el nombre del producto 
    precio_producto = primer_producto.find_element(By.CLASS_NAME, 'inventory_item_price') # asigno a la variable precio_producto el precio  del producto 

    assert nombre_producto.text == 'Sauce Labs Backpack', f'ERROR: El nombre del producto no se encontro o no es el mismo a, {nombre_producto}' # verifico que el texto de mombre_producto sea igual a Sauce Labs Backpack
    assert precio_producto.text == '$29.99', f'ERROR: Se esperaba $29.99 y se obtuvo, {precio_producto}' # verifico que el texto de precio_producto sea igual a $29.99



# test para validar que se muestren elementos en le intefaz del sitio 
def test_05_validar_interfaz(driver):

    menu_button = driver.find_element(By.ID, 'react-burger-menu-btn') # asigna a la variable menu_button el elemento menu hamburguesa
    filtro = driver.find_element(By.CLASS_NAME, 'product_sort_container')  # asigna a la variable filtro el elemento de filtro 

    assert menu_button.is_displayed(), f'ERROR El menu no esta visible ' # verifica si existe el elemento menu hamburguesa en el sitio 
    assert filtro.is_displayed(), f'ERROR El filtro no esta visible '   # verifica si existe el elemento filtro en el sitio 



#test 6 para agregar un producto al carrito 
def test_06_añadir_producto_al_carrito(driver):
    first_item = driver.find_elements(By.CLASS_NAME, 'inventory_item')[0] #agregar a la variable first_item el primer elemento de inventory_item

    boton_agregar = first_item.find_element(By.TAG_NAME, 'button') #agregar a la variable boton_agregar el elemento button su tagname
    boton_agregar.click()  # hacer click y agregar un elemnto al carrito 
   
    boton_actualizado = first_item.find_element(By.TAG_NAME, 'button')  # volver a buscar el elemento actualizado para evitar error cuando el dom y el driver de selenium maneja el elemento cuando cambia
    assert boton_actualizado.text.capitalize() == "Remove", f'ERROR: el boton no cambio a remove ' # verifica si el texto del boton es igual a la palabra Remove



#verificar si se agrego producto en el carrito 
def test_07_verificar_contador_carrito(driver):
    contador_carrito = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text #se asigna a la variable contador_carrito el texto con el valor del producto cargado en el carrito 

    assert contador_carrito == "1", f'ERROR: se esperaba 1 , obtuvo {contador_carrito}' #verifica si hay un elemento en el carrito de compras 



# test que verifica que se navega dentro de la pagina del carrito de compra /cart.html
def test_08_navegar_carrito(driver):
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click() # hace clik en el carrito para que se abra la pagina cart.html

    assert "/cart.html" in driver.current_url, "ERROR: No se reidirigio a la pagina /card.html" #verifica si esta en la pagina del carrito cart.html


# test luego de agregar producto navegar a la pagina del carrito y ver si se agrego el producto correctamente 
def test_09_comprobar_producto_en_carrito(driver):
    producto_nombre_carrito = driver.find_element(By.CLASS_NAME, 'inventory_item_name').text # asigna a la variable producto_nombre_carrito el texto Sauce Labs Backpack

    assert producto_nombre_carrito == "Sauce Labs Backpack", f'ERROR No se encontro el producto agregado Sauce Labs Backpack' # si el valor de la variable es igual a Sauce Labs Backpack el test paso 




    



