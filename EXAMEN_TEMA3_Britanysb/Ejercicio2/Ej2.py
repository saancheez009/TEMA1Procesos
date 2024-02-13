from threading import Thread
import random, time
from typing import Mapping

#Se utilizará barrier para el límite de dinero que entrará en la recaudación ya que no se puede superar los 2000
#en caso de superarse, el voluntario deberá esperar para ingresar lo recaudado

class Asociacion(Thread):
    
    def __init__(self, nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        #número aleatorio de dinero recaudado
        num=random.randint(4,25)
        
        print(self.name,"va a recaudar dinero")
        time.sleep(random.randint(1,3))
        #Cantidad recaudada por el voluntario
        print(self.name,"recauda",num,"€")
        
        

if __name__ == "__main__":
    hilos = []
    #El número máximo de voluntarios es 4
    for i in range(4):
        hilo = Asociacion(f"Voluntario-{i + 1}")
        hilos.append(hilo)
        hilo.start()


    for hilo in hilos:
        hilo.join()