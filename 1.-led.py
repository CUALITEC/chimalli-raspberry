import RPi.GPIO as GPIO #Importa Biblioteca GPIO de Raspberry Pi
import time #Importar librería de tiempo
LED = 7 #Se asigna pin
GPIO.setmode (GPIO.BCM) #Configuración
GPIO.setwarnings (False) #Anular Advertencias
GPIO.setup (LED, GPIO.OUT) # Se configura como salida

if __name__ == "__main__":
    for i in range (10): #Inicia ciclo for, para que se ejecute 10 veces el programa
        GPIO.output (LED, GPIO.LOW) #Encendido
        time.sleep (1) #Espera 1 segundo
        GPIO.output (LED, GPIO.HIGH) #Apagado
        time.sleep (1) #Espera 1 segundo
    