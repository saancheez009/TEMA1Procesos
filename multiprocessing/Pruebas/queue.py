from multiprocessing import*

def productor(cola):
    for i in range (1,11):
        cola.put(i)
    cola.put(None)
    
def consumidor(cola):
    objeto = cola.get()
    while objeto is not None:
        print(objeto)
        objeto= cola.get()
        

if __name__== "__main__":
    queue = Queue()
    p1= Process(target=productor, args=(queue))
    p2= Process(target=consumidor, args=(queue))
    
    p1.start()
    p2.start()
    
    p1.join()
    
queue.put(None)

p2.join()
print("Se han terminado los procesos")
    