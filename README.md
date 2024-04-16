# SaldoSube for Alexa
 Conoce el saldo de tu sube a través de tu dispositivo Amazon Alexa.

## ¿Cómo Funciona?
El programa hace uso de las bibliotecas de selenium para automatizar el inicio de sesión en la pagina de Sube.
Una vez logra iniciar sesión retorna el valor de tu saldo y lo envia a alexa usando la skill triggerCMD.

## ¿Cómo usar?
Requisitos
- [Python](https://www.python.org/downloads/)
- [Selenium 4.0 o posterior](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/)
- [Chrome webdriver](https://developer.chrome.com/docs/chromedriver/downloads?hl=es-419)
- [triggerCMD skill](https://www.triggercmd.com)

## Importante
Por ahora le programa solo funciona usando la skill de triggerCMD y ejecutando el script desde ahi, para eso es necesario tener configurada una computadora en triggerCMD y que esta este prendida para poder correr el script de python.

## FAQs
### ¿Qué es triggerCMD?
Es una [skill oficial de Alexa](https://www.amazon.com/gp/product/B074TV61DK) que permite ejecutar aplicaciones en tu pc usando comandos de voz a través de tu Alexa.

### ¿Cómo se configura triggerCMD?
Primero asegurate de activar la [skilll conversacional de triggerCMD](https://www.amazon.com/gp/product/B074TV61DK) llamada "Ejecuta Comando" una vez hecho eso tenes que [descargar la aplicación de escritorio para tu pc](https://triggercmd.com/es/)

Ya con eso solo falta configurar qué comando queres que se ejecute en tu compu cuando uses la skill desde Alexa

La mia por ejemplo es asi:
```
 {
  "trigger": "saldo",
  "command": "python C:\\alexaSube\\src\\main.py",
  "offCommand": "",
  "ground": "foreground",
  "voice": "saldo",
  "voiceReply": "El saldo de tu sube es {{result}} pesos",
  "allowParams": "false"
 }
```

Esto significa que cuando le diga a su Alexa "Ejecuta comando saldo" va a ejecutar el comando "python C:\\alexaSube\\src\\main.py" en sus computadoras.