from gpiozero import Servo #Importar librerías
from time import sleep #Importar librería de tiempo
servo_1 = Servo (12) #Se asigna pin de salida

if __name__ == "__main__":
    while True: #Ciclo while
        servo_1.min () #Movimiento mínimo
        sleep(2) #Espera
        servo_1.mid() #Movimiento medio
        sleep(2) #Espera
        servo_1.max () #Movimiento Máximo
        sleep(2) #Espera