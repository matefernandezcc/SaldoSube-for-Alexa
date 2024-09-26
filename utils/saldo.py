import time
from playwright.sync_api import sync_playwright
import os
import subprocess

###################### Ruta absoluta ######################
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(script_dir, 'data.txt')

###################### Leer data.txt ######################
with open(data_file_path, 'r') as file:
    ########### Obtener el documento y la contraseña ###########
    lines = file.readlines()
    documento = lines[0].strip()
    password = lines[1].strip()

###################### Intentar obtener el saldo ######################
def get_balance():
    while True:
        try:
            with sync_playwright() as p:
                ########### Navegador ###########
                browser = p.chromium.launch(headless=False, args=['--no-sandbox'])
                page = browser.new_page()

                ########### Login page ###########
                page.goto('https://tarjetasube.sube.gob.ar/SubeWeb/WebForms/Account/Views/Login.aspx')

                page.fill('input#txtDocumento', documento)
                page.get_by_text('MASCULINO').click()
                page.fill('input#txtPassword', password)

                ########### Intentar hacer click en el botón de ingresar ###########
                page.get_by_role('button', name='Ingresar').click()

                ########### Esperar a que el iframe de reCAPTCHA esté visible ###########
                captcha_frame_selector = "iframe[title='El reCAPTCHA caduca dentro de dos minutos']"
                page.wait_for_selector(captcha_frame_selector) 

                ########### Verificar si el iframe de reCAPTCHA está presente ###########
                if page.locator(captcha_frame_selector).is_visible():
                    to_alexa("Se detectó un Captcha, no pude obtener el saldo")
                    browser.close()
                    return

                ########### Esperar al elemento del saldo ###########
                page.wait_for_selector('span.ng-binding.font-saldo.bold')
                balance_text = page.locator('span.ng-binding.font-saldo.bold').text_content()

                ########### Verificar que el balance sea un número ###########
                if balance_text:
                    balance_text = balance_text.replace(',', '.').replace('$', '').replace(' ', '').strip()
                    # Solo devolver el saldo si se convierte correctamente
                    if balance_text:
                        return float(balance_text)

                ########### Si no se encuentra el saldo, vuelve a intentar ###########
                browser.close()
                time.sleep(2)

        except Exception as e:
            print(f"Error: {e}")  # Imprimir el error para depuración
            time.sleep(2)

###################### FUNCION PARA ENVIAR MENSAJES A ALEXA ######################
def to_alexa(message):
    comando = '/mnt/c/Users/Mateo/Desktop/test/repos-github/SaldoSube-for-Alexa/SaldoSube-for-Alexa/alexa-remote-control/alexa_remote_control.sh'
    argumentos = ['-e', f'speak:{message}']
    
    resultado = subprocess.run([comando] + argumentos, capture_output=True, text=True)

###################### Llamar a la función y almacenar el saldo ######################
if __name__ == "__main__":
    saldo = get_balance()
    print(saldo)
