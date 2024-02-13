from threading import Thread, Semaphore, Event
import time, random

#He elegido como método de sincronización Semaphore ya que para utilizar las máquinas o ser atendidos los clientes deberan esperar hasta que una de las máquinas estén libres
#, si están ocupadas se bloquean, para que los clientes sean atendidos por los dependientes ocurre lo mismo.

class Hamburgueseria(Thread):
    #número de máquinas, semáforo
    maquinas = Semaphore(2)
    #número de dependientes, semáforo
    dependientesem= Semaphore(5)
    
    def __init__(self,nombre, event:Event):
        Thread.__init__(self, name=nombre)
        self.evento=Event
    
    def run(self):
        #El cliente espera hasta que la máquina esté libre 
        while not self.evento.is_set():
            self.evento.wait()
        self.evento.clear()
        #Cliente va a una máquina que esté libre
        print(self.name,"va a una máquina ")
        Hamburgueseria.maquinas.acquire()
        print(self.name,"está sacando el ticket")
        #tiempo de espera aleatorio hasta que la máquina le da el ticket al cliente
        time.sleep(random.randint(1,4))
        print(self.name,"tiene el ticket ")
        Hamburgueseria.maquinas.release()
        #Cliente va al mostrador a por su pedido
        print(self.name,"va al mostrador")
        #El dependiente que esté libre lo atiende y prepara su pedido, si no hay dependientes libres , el cliente espera
        Hamburgueseria.dependientesem.acquire()
        print(self.name,"está siendo atendido")
        #tiempo de espera aleatorio hasta que el dependiente pepara el pedido al cliente
        time.sleep(random.randint(3,7))
        print(self.name,"ya tiene su hamburguesa")
        Hamburgueseria.dependientesem.release()
        print(self.name,"se va de la hamburgueseria")
        #Elcliente tiene su pedido y se va de la hamburguesería
        self.evento.set()

if __name__ == "__main__":
    hilos = []
    #El número máximo de clientes que van a la hamburguesería es 10
    for i in range(10):
        hilo = Hamburgueseria(f"Cliente-{i + 1}")
        hilos.append(hilo)
        hilo.start()


    for hilo in hilos:
        hilo.join()
    
    
    
    
