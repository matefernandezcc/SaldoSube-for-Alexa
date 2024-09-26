# SaldoSube for Alexa
Conoce el saldo de tu SUBE a través de tu dispositivo Amazon Alexa.

<div align="center">
    <img src="https://www.mendoza.gov.ar/wp-content/uploads/sites/5/2019/10/post-SUBE-1-01.png" alt="SUBE" style="width: 500px; height: auto;">
</div>

## ¿Cómo Funciona?
El programa hace uso del navegador de Playwright para automatizar el inicio de sesión en la página de SUBE. Una vez logra iniciar sesión, retorna el valor de tu saldo y se lo envía a Alexa usando [Alexa-remote-control](https://github.com/adn77/alexa-remote-control), el cual es un programa que permite manejar a Alexa desde una terminal.

## ¿Cómo usar?
### Requisitos
- [Python](https://www.python.org/downloads/)
- [Playwright](https://playwright.dev/python/docs/intro)
- [Setup - Alexa remote control](https://github.com/adn77/alexa-remote-control)
- [Opcional - Alexa triggerCMD skill](https://www.triggercmd.com)

## Importante
Para que el programa funcione, tienen que haber configurado previamente Alexa remote control, siguiendo las [instrucciones](https://github.com/adn77/alexa-remote-control). Pero, básicamente, tienen que descargar el binario de [Alexa Cookie CLI](https://github.com/adn77/alexa-cookie-cli/releases).

1. Ejecutar alexa-cookie-cli
2. En el navegador, ingresar a http://127.0.0.1:8080/
3. Iniciar sesión en Amazon
4. Si todo salió bien, el programa mostrará en la terminal su `refresh_token` (empieza con Atnr|...)

Una vez tengan el `refresh_token`, lo copian y pegan dentro del archivo alexa-remote-control donde dice `SET_REFRESH_TOKEN='lo pegan aca'`.

## FAQs
### ¿Cómo uso el script?
Luego de haber configurado todo, solo queda que cambies los `PATH` dentro del archivo `main.py` y listo. Uno debería ir hacia `saldo.py` y el otro hacia `alexa_remote_control.sh`.

### ¿Qué es triggerCMD?
Es una [skill oficial de Alexa](https://www.amazon.com/gp/product/B074TV61DK) que permite ejecutar comandos por cmd en tu PC usando comandos de voz a través de tu Alexa. Es útil para ejecutar el script directamente usando tu voz sin tener que correrlo desde la PC.

### ¿Cómo se configura triggerCMD?
Primero asegúrate de activar la [skill conversacional de triggerCMD](https://www.amazon.com/gp/product/B074TV61DK) llamada "Ejecuta Comando". Una vez hecho eso, tienes que [descargar la aplicación de escritorio para tu PC](https://triggercmd.com/es/).

Ya con eso solo falta configurar qué comando quieres que se ejecute en tu compu cuando uses la skill desde Alexa.

Por ejemplo, si tu configuración en triggerCMD es así:
```json
{
  "trigger": "saldo",
  "command": "python C:\\alexaSube\\src\\main.py",
  "offCommand": "",
  "ground": "foreground",
  "voice": "saldo",
  "voiceReply": "",
  "allowParams": "false"
}

Esto significa que al decirle a Alexa "Ejecuta comando saldo", va a ejecutar en tu pc -> "python C:\\alexaSube\\src\\main.py"
