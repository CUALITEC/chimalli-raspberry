import Rpi.GPIO as GPIO #Importar librerías
import time #Importar librería de tiempo
GPIO.setmode (GPIO.BCM) #Configuración
GPIO.setwarnings (False) #Anular Advertencias
BUZZER = 18 #Asignación de Pin
GPIO.setup (BUZZER, GPIO.OUT) #Se configura la salida

if __name__ == "__main__":
    while True: #Ciclo While
        GPIO.output (BUZZER, GPIO.HIGH) #Ponemos en alto el pin del Buzzer
        time.sleep (1) #Esperamos un segundo antes de ejecutar la siguiente línea
        GPIO.output (BUZZER, GPIO.LOW) #Ponemos en bajo el pin del Buzzer
        time.sleep (4) #Esperamos cuatro segundos antes de ejecutar la siguiente linea