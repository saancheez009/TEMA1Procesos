from multiprocessing import*

def process1(extremo1):
    extremo1.send("Proceso 1 envía mensaje")

def process2(extremo2):
    mensaje = extremo2.recv()
    print(mensaje)

if __name__=="__main__":
    izq,der = Pipe()
    
    p1= Process(target=process1, args=(izq,))
    p2= Process(target=process2, args=(der,))
    
    p1.start()
    p2.start()
    