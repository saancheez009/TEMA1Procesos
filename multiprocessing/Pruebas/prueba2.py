from multiprocessing import*
import time

def hello(name):
    print("Hello world",name)
    
    
def suma(num1,num2):
    res = num1 + num2
    print("Suma igual a ",res)
    
if __name__ == "__main__":
    p1 = Process(target = suma, args=(3,5))
    p2 = Process(target=hello, args=("Britany",))
    p1.start()
    p2.start()
    
    fin=time.time()
    print("Tiempo:",fin-inicio)
        