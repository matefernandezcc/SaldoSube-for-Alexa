from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os
import time

# Ruta del archivo de saldo
saldo_file = 'main\\saldo.txt'

# Leer el saldo anterior y enviarlo a Alexa
saldo = open(saldo_file, 'r').read().strip()
os.system(os.environ['USERPROFILE'] + "\\.TRIGGERcmdData\\SendResult.bat "+str(saldo))
print("El saldo enviado a Alexa fue:", saldo)

try:
    # Leer el saldo nuevo
    if os.path.exists(saldo_file):
        with open(saldo_file, 'r') as file:
            saldo = file.read().strip()
            if saldo:
                saldo = float(saldo)
            else:
                saldo = None
    else:
        saldo = None

    # Path donde está el WebDriver de Chrome
    service = Service(r"PATH A TU WEBDRIVER")

    # Configurar las opciones del navegador Chrome
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')  

    # Inicializar el WebDriver de Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # URL de la página de sube
    url = "https://tarjetasube.sube.gob.ar/SubeWeb/WebForms/Account/Views/Login.aspx"

    # Abrir la página de inicio de sesión
    driver.get(url)

    # Llenar los campos de inicio de sesión
    tipo_documento = driver.find_element(By.ID, "ddlTipoDocumento")
    tipo_documento.send_keys("DNI")
    numero_documento = driver.find_element(By.ID, "txtDocumento")
    numero_documento.send_keys("ACA VA TU NÚMERO DE DNI")
    driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "switch_right"))
    contraseña = driver.find_element(By.ID, "txtPassword")
    contraseña.send_keys("ACA VA TU CONTRASEÑA")

    # Hacer clic en el botón de inicio de sesión
    boton_inicio_sesion = driver.find_element(By.XPATH, "//button[@data-ng-click='LoginRecaptcha()']")
    boton_inicio_sesion.click()

    time.sleep(5) # Esperar para que se cargue bien la página

    # 10 intentos para leer el saldo
    max_attempts = 10
    current_attempt = 0
    saldo_obtenido = False

    while current_attempt < max_attempts and not saldo_obtenido:
        try:
            # Encontrar el elemento que contiene el saldo
            saldo_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='ng-binding font-size-m text-primary text-success bold']")))

            # Obtener el texto del saldo
            saldo_str = saldo_element.text.strip().replace("$", "").replace(".", "").replace(",", ".")
            if saldo_str:
                saldo = float(saldo_str)
                saldo_obtenido = True
            else:
                print("El saldo obtenido está vacío o no se terminó de cargar la página")

        except Exception as e:
            # Si hay algún error al obtener el saldo, imprimirlo y continuar
            print("Error al obtener el saldo en el intento", current_attempt + 1, ":")

        current_attempt += 1

    # Si se pudo obtener el saldo correctamente lo actualiza en el archivo saldo.txt
    if saldo_obtenido:
        with open(saldo_file, 'w') as file:
            file.write(str(saldo))
        print("El saldo se actualizó correctamente en el archivo saldo.txt:", saldo)

except Exception as e:
    print("Se produjo un error al obtener el saldo")

finally:
    # Cerrar el navegador
    if 'driver' in locals():
        driver.quit()
