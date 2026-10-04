from selenium.webdriver.common.by import By # clases common del webdriver pro medio del by



def login(driver):
    
    driver.get("https://www.saucedemo.com/") #con get accede a la pagina y abre el navegador con la url 

    driver.find_element(By.ID, "user-name").send_keys("standard_user") #encuentra con metodo find_element mediante un selector en este caso ID el username
    driver.find_element(By.ID, "password").send_keys("secret_sauce") #encuentra con metodo find_element mediante un selector en este caso ID el password
    driver.find_element(By.ID, "login-button").click() #encuentra con metodo find_element mediante un selector en este caso el evento click del boton 

