from gpiozero import Button #Importar librerías de Botones
from time import sleep #Importar librerías de tiempo

left = Button(2,True) #Asignacion de pin y declaración de estado del pin
up = Button(3,True) #Asignacion de pin y declaración de estado del pin
right = Button(6,False) #Asignacion de pin y declaración de estado del pin
down = Button(17,False) #Asignacion de pin y declaración de estado del pin

if __name__ == '__main__': #Se declara sentencia if
    while True: #Inicia ciclo while
        if left.is_pressed: #Sentencia if para saber si se presiono el boton
            print('Boton LEFT presionado') #Texto a imprimir al momento en que se detecta elboton oprimido
            sleep(0.4) #Tiempo de espera
        elif up.is_pressed: #Sentencia elif para saber si se presiono el boton
            print('Boton Up presionado') #Texto a imprimir al momento en que se detecta el boton oprimido
            sleep(0.4) #Tiempo de espera
        elif right.is_pressed: #Sentencia elif para saber si se presiono el boton
            print('Boton RIGHT presionado') #Texto a imprimir al momento en que se detecta elboton oprimido
            sleep(0.4) #Tiempo de espera
        elif down.is_pressed: #Sentencia elif para saber si se presiono el boton
            print('Boton DOWN presionado') #Texto a imprimir al momento en que se detecta el boton oprimido
            sleep(0.4) #Tiempo de espera
        else: #Sentencia else para saber si se presiono el boton
            print('Esperando') #Texto a imprimir si ningun boton es oprimido
            sleep(0.4) #Tiempo de espera