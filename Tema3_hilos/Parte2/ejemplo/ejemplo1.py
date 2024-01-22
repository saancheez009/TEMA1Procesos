from asyncio import Semaphore
import random
from threading import Thread
import time

class Cajero(Thread):
    semaforo = Semaphore(4)
    
    def __init__(self,nombre):
        Thread.__init__(self, name=nombre)
        
    def run(self):
        print("El hilo", self.name, "está comprando")
        Cajero.semaforo.acquire()
        print("El hilo", self.name, "está en caja ")
        time.sleep(random.randint(1,10))
        print("El hilo ", self.name, "ya ha pagado")
        Cajero.semaforo.release()