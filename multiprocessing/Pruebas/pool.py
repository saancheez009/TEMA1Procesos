from multiprocessing import*

def square(number):
    """Función que calcula el cuadrado de un número"""
    
    return number*number

if __name__=="__main__":
    with Pool(processes=3) as pool:
        numbers = [1,2,3,4,5]
        
        results = pool.map(square,numbers)
        
    print("Resultados: ",results)