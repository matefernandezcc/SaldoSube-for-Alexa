from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import subprocess
import time
import locale
from datetime import datetime

# ////////////////////////////////// Leer el archivo .env //////////////////////////////////
load_dotenv()
DNI = os.getenv("DNI")
PIN = os.getenv("PIN")
GENERO = os.getenv("GENERO")

# ////////////////////////////////// Función para guardar el saldo y la fecha //////////////////////////////////
def guardar(saldo):
    # Obtener la fecha en formato más humano
    current_time = datetime.now()
    fecha_humana = current_time.strftime("%d de %B de %Y a las %H horas y %M minutos")  # Formato: 21 de marzo de 2025 a las 15 horas 30 minutos
    
    with open("saldo_record.txt", "w") as file:
        file.write(f"{fecha_humana}\n{saldo}")

# ////////////////////////////////// Función para leer el saldo guardado //////////////////////////////////
# Establecer el locale en español para guardar fechas con meses en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

def ultimo_saldo():
    try:
        with open("saldo_record.txt", "r") as file:
            fecha = file.readline().strip()
            ultimo_saldo = file.readline().strip()
            return fecha, ultimo_saldo
    except FileNotFoundError:
        return None, None

# ////////////////////////////////// Intentar obtener el saldo //////////////////////////////////
def get_balance():
    while True:
        try:
            with sync_playwright() as p:
                # //////////// Navegador ////////////
                browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
                page = browser.new_page()

                # //////////// Login page ////////////
                page.goto('https://tarjetasube.sube.gob.ar/SubeWeb/WebForms/Account/Views/Login.aspx')
                # Rellenar información
                page.fill('input#txtDocumento', DNI)
                page.get_by_text(f'{GENERO}').click()
                page.fill('input#txtPassword', PIN)

                # //////////// Intentar hacer click en el botón de ingresar ////////////
                page.get_by_role('button', name='Ingresar').click()

                # //////////// Esperar a que el iframe de reCAPTCHA esté visible ////////////
                captcha_frame_selector = "iframe[title='El reCAPTCHA caduca dentro de dos minutos']"
                try:
                    page.wait_for_selector(captcha_frame_selector, timeout=10000)  # Esperar 10 segundos por si aparece un captcha
                except Exception:
                    pass

                # //////////// Verificar si el iframe de reCAPTCHA está presente ////////////
                if page.locator(captcha_frame_selector).is_visible():
                    to_alexa("Se detectó un Captcha, no pude obtener el saldo")
                    print("Se detectó un Captcha, no pude obtener el saldo")
                    fecha, saldo_guardado = ultimo_saldo()  # Solo leer saldo guardado si falla
                    time.sleep(3)
                    if fecha and saldo_guardado:
                        to_alexa(f"El último saldo hasta la fecha fue de {saldo_guardado} pesos, obtenido el día {fecha}")
                        print(f"El último saldo hasta la fecha fue de {saldo_guardado} pesos, obtenido el día {fecha}")
                    time.sleep(2)
                    browser.close()
                    exit(1)

                # //////////// Esperar al elemento del saldo ////////////
                page.wait_for_selector('span.ng-binding.font-saldo.bold')
                balance_text = page.locator('span.ng-binding.font-saldo.bold').text_content()

                # //////////// Verificar que el balance sea un número ////////////
                if balance_text:
                    balance_text = balance_text.replace('$', '').replace(' ', '').strip()
                    guardar(balance_text) # Registrar saldo
                    return balance_text

                # //////////// Si no se encuentra el saldo, vuelve a intentar ////////////
                browser.close()
                time.sleep(2)

        except Exception as e:
            fecha, saldo_guardado = ultimo_saldo()
            if fecha and saldo_guardado:
                to_alexa(f"El último saldo hasta la fecha fue de {saldo_guardado} pesos, obtenido el día {fecha}")
            print(f"Error: {e}")  # Imprimir el error para depuración
            time.sleep(2)

# ////////////////////////////////// Wrapper para enviar mensajes a Alexa //////////////////////////////////
def to_alexa(message):
    path = './alexa-remote-control/alexa_remote_control.sh'
    argumento = ['-e', f'speak:{message}']

    resultado = subprocess.run([path] + argumento, capture_output=True, text=True)

# ////////////////////////////////// Llamar a la función y almacenar el saldo //////////////////////////////////
if __name__ == "__main__":
    saldo = get_balance()
    print(saldo)