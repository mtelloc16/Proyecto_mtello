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
driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(2)
# Seleccionar "MacBook Pro"
driver.find_element(By.LINK_TEXT, "MacBook Pro").click()
time.sleep(2)
# Agregar al carrito
driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
# Volver al inicio
driver.get("https://www.demoblaze.com")
time.sleep(2)
# Ir a la categoría "Phones"
driver.find_element(By.LINK_TEXT, "Phones").click()
time.sleep(2)
# Seleccionar "Nokia lumia 1520"
driver.find_element(By.LINK_TEXT, "Nokia lumia 1520").click()
time.sleep(2)
# Agregar al carrito
driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
# Ir al carrito
driver.find_element(By.ID, "cartur").click()
time.sleep(2)
# Iniciar la compra
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(2)
# Esperar que aparezca el formulario
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "name")))
# Llenar el formulario
driver.find_element(By.ID, "name").send_keys("María Fernanda")
driver.find_element(By.ID, "country").send_keys("Ecuador")
driver.find_element(By.ID, "city").send_keys("Quito")
driver.find_element(By.ID, "card").send_keys("1234 5678 9101 1121")
driver.find_element(By.ID, "month").send_keys("12")
driver.find_element(By.ID, "year").send_keys("2025")
# Confirmar la compra
boton_purchase = driver.find_element(By.XPATH, "//button[text()='Purchase']")
boton_purchase.click()
time.sleep(2)
# Confirmar mensaje de éxito (opcional)
mensaje = driver.find_element(By.CLASS_NAME, "sweet-alert").text
print("Mensaje de confirmación:")
print(mensaje)
# Cerrar el navegador
driver.quit()