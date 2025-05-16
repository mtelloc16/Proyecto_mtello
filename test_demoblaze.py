from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Ruta local de chromedriver
ruta_chromedriver = "C:\\Users\\mtello\\Desktop\\Demoblaze\\chromedriver\\chromedriver.exe"
service = Service(ruta_chromedriver)
driver = webdriver.Chrome(service=service)
# Abrir el sitio web de Demoblaze
driver.get("https://www.demoblaze.com")
time.sleep(2)
# Ir a la categoría "Laptops"
categoria_laptops = driver.find_element(By.LINK_TEXT, "Laptops")
categoria_laptops.click()
time.sleep(2)
# Seleccionar "MacBook Pro"
producto1 = driver.find_element(By.XPATH, "//a[text()='MacBook Pro']")
producto1.click()
time.sleep(2)
# Agregar al carrito
boton_agregar1 = driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']")
boton_agregar1.click()
time.sleep(2)
# Aceptar la alerta de agregar al carrito
driver.switch_to.alert.accept()
time.sleep(2)
# Volver a la página principal y seleccionar otro producto
driver.get("https://www.demoblaze.com")
time.sleep(2)
# Seleccionar "Nokia lumia 1520"
producto2 = driver.find_element(By.XPATH, "//a[text()='Nokia lumia 1520']")
producto2.click()
time.sleep(2)
# Agregar al carrito
boton_agregar2 = driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']")
boton_agregar2.click()
time.sleep(2)
# Aceptar la alerta
driver.switch_to.alert.accept()
time.sleep(2)
# Ir al carrito
carrito = driver.find_element(By.ID, "cartur")
carrito.click()
time.sleep(2)
# Iniciar la compra
boton_comprar = driver.find_element(By.XPATH, "//button[@class='btn btn-success']")
boton_comprar.click()
time.sleep(2)
# Esperar hasta que el formulario esté visible
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.ID, "name")))
# Completar formulario con datos
driver.find_element(By.ID, "name").send_keys("María Fernanda")
driver.find_element(By.ID, "country").send_keys("Ecuador")
driver.find_element(By.ID, "city").send_keys("Quito")
driver.find_element(By.ID, "card").send_keys("1234 5678 9101 1121")
driver.find_element(By.ID, "month").send_keys("12")
driver.find_element(By.ID, "year").send_keys("2025")
# Esperar y hacer scroll hasta el botón 'Purchase'
boton_confirmar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Purchase']")))
driver.execute_script("arguments[0].scrollIntoView(true);", boton_confirmar)
boton_confirmar.click()
time.sleep(3)
# Confirmación de compra realizada
print("Compra realizada con éxito.")
# Cerrar el navegador
driver.quit()