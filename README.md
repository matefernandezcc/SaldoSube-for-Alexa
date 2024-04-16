# SaldoSube for Alexa
 Conoce el saldo de tu sube a través de tu dispositivo Amazon Alexa

## ¿Cómo Funciona?
El programa hace uso de las bibliotecas de selenium para automatizar el inicio de sesión en la pagina de Sube
Una vez logra iniciar sesión retorna el valor de tu saldo y lo envia a alexa usando la skill triggerCMD.

## ¿Cómo usar?
Requisitos
- [Python](https://www.python.org/downloads/)
- [Selenium 4.0 o posterior](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)
- [Chrome webdriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=es-419)
- [triggerCMD skill](https://www.triggercmd.com)

## Importante
Por ahora le programa solo funciona usando la skill de triggerCMD y ejecutando el script desde ahi, para eso es necesario tener configurada una computadora en triggerCMD y que esta este prendida para poder correr el script de python.