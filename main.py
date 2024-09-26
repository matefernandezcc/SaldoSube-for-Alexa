import subprocess
import sys
import os

###################### saldo.py debe retornar un string ######################
def get_saldo():
    try:
        ########### Ejecutar el script saldo.py y obtener su salida ###########
        result = subprocess.run(['python', '/mnt/c/Users/Mateo/Desktop/test/repos-github/SaldoSube-for-Alexa/SaldoSube-for-Alexa/utils/saldo.py'], 
                                 capture_output=True, text=True, check=True)
        
        ########### Obtener el saldo como string ###########
        saldo = result.stdout.strip()
        return saldo
    except subprocess.CalledProcessError as e:
        err1 = f'/mnt/c/Users/Mateo/Desktop/test/repos-github/SaldoSube-for-Alexa/SaldoSube-for-Alexa/alexa-remote-control/alexa_remote_control.sh -e "speak:Hubo un error al obtener el saldo"'
        subprocess.run(err1, shell=True, check=True, capture_output=True, text=True)
        sys.exit(1)

###################### Ejecutar el script de bash con el saldo obtenido ######################
def run_alexa_remote_control(saldo):
    # Convertir el saldo a string y formatearlo si es necesario
    saldo_str = str(saldo).replace('.', ',')
    command = f'/mnt/c/Users/Mateo/Desktop/test/repos-github/SaldoSube-for-Alexa/SaldoSube-for-Alexa/alexa-remote-control/alexa_remote_control.sh -e "speak:Tu saldo es de {saldo_str}"'
    
    try:
        ########### Ejecutar el script de bash ###########
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("Salida del script de Alexa Remote Control:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        err2 = f'/mnt/c/Users/Mateo/Desktop/test/repos-github/SaldoSube-for-Alexa/SaldoSube-for-Alexa/alexa-remote-control/alexa_remote_control.sh -e "speak:Hubo un error al ejecutar alexa remote"'
        subprocess.run(err2, shell=True, check=True, capture_output=True, text=True)
        sys.exit(1)

if __name__ == "__main__":
    saldo = get_saldo()
    run_alexa_remote_control(saldo)
