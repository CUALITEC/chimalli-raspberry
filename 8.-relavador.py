from gpiozero import LED as RELEVADOR#Importar librerías
from time import sleep #Importar librería de tiempo

rele_1 = RELEVADOR(4) #Asignacion de pin
rele_2 = RELEVADOR(5) #Asignacion de pin
rele_3 = RELEVADOR(6) #Asignacion de pin
rele_4= RELEVADOR(17) #Asignacion de pin
tiempo = 1 #Asignacion de tiempo a la variable

def activar_relevadores(): #Se define la función blink
    rele_2.on() #Relevador 2 apagado
    rele_3.on() #Relevador 3 apagado
    rele_4.on() #Relevador 4 apagado
    rele_1.off() #Relevador 1 encendido
    sleep(tiempo) #Tiempo de espera
    rele_1.on() #Relevador 1 apagado
    sleep(tiempo) #Tiempo de espera

if __name__ == '__main__': #Declaración de sentencia para que el programa se ejecute constantemente
    while True:
        activar_relevadores()