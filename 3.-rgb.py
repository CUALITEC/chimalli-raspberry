from gpiozero import RGBLED #Importar librería
from time import sleep #Importar librería de tiempo
led_rgb = RGBLED (red = 21, green = 20, blue = 19) #Se crea el modulo del led RGB

def colores_base():
    #Todos apagados
    led_rgb.color = (1, 1, 1)
    sleep(1)
    #Rojo máxima intensidad
    led_rgb.color = (0, 1, 1)
    sleep(1)
    #verde máxima intensidad
    led_rgb.color = (1, 0, 1)
    sleep(1)
    #Azul máxima intensidad
    led_rgb.color = (1, 1, 0)
    sleep(1)

if __name__ == '__main__':
    while True:
        colores_base()