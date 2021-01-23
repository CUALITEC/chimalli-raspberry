from gpiozero import PWMLED#Importar librerías
from gpiozero import MCP3008
from time import sleep #Importar librería de tiempo
pot = MCP3008 (0) #Asignación del canal a leer
led = PWMLED (7) #Se asigna pin de salida

if __name__ == "__main__":
    while True: #Ciclo while
        if (pot.value<0.002):
            led.value = 0
        else:
            led.value = pot.value
        print (pot.value) #Imprime el valor analógico leído
        sleep (0.1) #Tiempo de esperar para volver a leer el valor