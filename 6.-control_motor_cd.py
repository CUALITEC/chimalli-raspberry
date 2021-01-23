from gpiozero import LED as MOTOR #Importar librerías
from time import sleep #Importar librería de tiempo
motor_B_polo_1 = MOTOR (27) #Asignación de Pin
motor_B_polo_2 = MOTOR (22) #Asignación de Pin

def adelante (): #Función para mover el motor en sentido horario
    motor_B_polo_1.on ()
    motor_B_polo_2.off ()
def atras (): #Función para mover el motor en sentido anti horario
    motor_B_polo_1.off ()
    motor_B_polo_2.on ()
def paro (): #Función para detener el motor
    motor_B_polo_1.off ()
    motor_B_polo_2.off ()

if __name__ == '__main__':
    while True: #Ciclo While
        adelante ()
        sleep(1)
        paro ()
        sleep (1)
        atras ()
        sleep (1)
        paro ()
        sleep (3)