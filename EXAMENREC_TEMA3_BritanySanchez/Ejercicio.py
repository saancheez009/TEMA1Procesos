import random
import time
from threading import Condition, Thread

class AccesoColores(Thread):
    #utilizo condition ya que cada persona intentará tomar un color 
         
    lista=[False, False, False, False, False]
    cond = Condition()
    
    def __init__(self,nombre):
        Thread.__init__(self,name=nombre)
       
    
    def run(self):
   
        amarillo="amarillo"
        magenta="magenta"
        cian="cian"
        num=random.randint(0,5)
        
        AccesoColores.lista[num]== True:
            
        
        print("Claudia",self.name, "va a preparar el color rojo")
        print("Claudia",self.name, "coge el",amarillo)
        time.sleep(random.randrange(0.1,0.5))
        print("Claudia",self.name, "coge el",magenta)
        time.sleep(random.randrange(0.1,0.5))
        
        print("Randi",self.name,"va a preparar el color azul")
        print("Randi",self.name, "coge el",cian)
        time.sleep(random.randrange(0.1,0.5))
        print("Randi",self.name, "coge el",magenta)
        time.sleep(random.randrange(0.1,0.5))
        
        print("Fani",self.name,"va a preparar el color verde")
        print("Fani",self.name, "coge el",amarillo)
        time.sleep(random.randrange(0.1,0.5))
        print("Fani",self.name, "coge el",cian)
        time.sleep(random.randrange(0.1,0.5))
        
        
        
        
    


