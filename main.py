import subprocess
import sys
from utils.saldo import *

###################### Ejecutar el script de bash con el saldo obtenido ######################
def format_saldo(saldo):
    saldo_str = str(saldo).replace('.', ',')
    
    try:
        to_alexa(f"Tu saldo es de {saldo_str} pesos")
        #print(f"Tu saldo es de {saldo_str} pesos")

    except subprocess.CalledProcessError as e:
        to_alexa("Hubo un error al ejecutar Alexa remote")
        sys.exit(1)

if __name__ == "__main__":
    to_alexa("Obteniendo Saldo...")
    saldo = get_balance()
    format_saldo(saldo)