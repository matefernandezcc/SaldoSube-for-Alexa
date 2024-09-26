# SaldoSube for Alexa
 Conoce el saldo de tu sube a través de tu dispositivo Amazon Alexa.
 
 <br>
 <div style="text-align: center;">
    <img src="https://www.mendoza.gov.ar/wp-content/uploads/sites/5/2019/10/post-SUBE-1-01.png" alt="SUBE" style="width: 500px; height: auto;">
</div>

## ¿Cómo Funciona?
El programa hace uso del navegador de Playwright para automatizar el inicio de sesión en la pagina de Sube.
Una vez logra iniciar sesión retorna el valor de tu saldo y se lo envia a Alexa usando [Alexa-remote-control](https://github.com/adn77/alexa-remote-control) el cual es un programa que permite manejar a Alexa dede una terminal.

## ¿Cómo usar?
Requisitos
- [Python](https://www.python.org/downloads/)
- [Playwright](https://playwright.dev/python/docs/intro)
- [Setup - Alexa remote control](https://github.com/adn77/alexa-remote-control)
- [Opcional - Alexa triggerCMD skill](https://www.triggercmd.com)

## Importante
Para que el programa funcione tienen que previamente haber configurado Alexa remote control, siguiendo las [intrucciones](https://github.com/adn77/alexa-remote-control), pero básicamente tienen que descargar el binario de 
[Alexa Cookie CLI](https://github.com/adn77/alexa-cookie-cli/releases).

 1 Ejecutar alexa-cookie-cli
 2 En el navegador ingresar a http://127.0.0.1:8080/
 3 Iniciar sesión en Amazon
 4 Si todo salío bien, el programa va a mostrar en la terminal su refresh_token (empieza con Atnr|...)

Una vez tienen el refresh_token lo copian y pegan dentro del archivo alexa-remote-control donde dice SET_REFRESH_TOKEN='lo pegan aca'

## FAQs
### ¿Cómo uso el script?
Luego de haber configurado todo solo queda que cambies los PATH dentro del archivo main.py y listo.
Uno deberia ir hacia saldo.py y el otro hacia alexa_remote_control.sh

### ¿Qué es triggerCMD?
Es una [skill oficial de Alexa](https://www.amazon.com/gp/product/B074TV61DK) que permite ejecutar comandos por cmd en tu pc usando comandos de voz a través de tu Alexa.
Es útil para ejecutar el script directamente usando tu voz sin tener que correrlo desde la pc.

### ¿Cómo se configura triggerCMD?
Primero asegurate de activar la [skill conversacional de triggerCMD](https://www.amazon.com/gp/product/B074TV61DK) llamada "Ejecuta Comando" una vez hecho eso tenes que [descargar la aplicación de escritorio para tu pc](https://triggercmd.com/es/)

Ya con eso solo falta configurar qué comando queres que se ejecute en tu compu cuando uses la skill desde Alexa

Por ejemplo si tu config en triggerCMD es asi:
```
 {
  "trigger": "saldo",
  "command": "python C:\\alexaSube\\src\\main.py",
  "offCommand": "",
  "ground": "foreground",
  "voice": "saldo",
  "voiceReply": "",
  "allowParams": "false"
 }
```

Esto significa que cuando le digas a Alexa "Ejecuta comando saldo" va a ejecutar el comando "python C:\\alexaSube\\src\\main.py" en tu computadora.
