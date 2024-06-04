from multiprocessing import Process, Queue
#proceso 1 recibe la categoria del refran para mandar al proceso 2 los refranes de esa categoria
def proceso1(ruta, categoria, output_queue):
    with open(ruta, 'r') as file:
        lines = file.readlines()
        categorias = [line.strip() for line in lines if line.split(';')[-1].strip() == str(categoria)]
        output_queue.put(categorias)

#proceso2 recibe los refranes de una cat especifica y elimina de las lineas la categoria
def proceso2(output_queue,cola2):
    refranes=[]
    while not output_queue.empty():
        refranes.extend(output_queue.get())
    
    if refranes:
        categoria = refranes[0].split(';')[-1].strip()
        while True:
            if refranes is None:
                cola2.put(None)
                break
            refran_completo, _ = refranes.rsplit(' ;', 2)
            cola2.put(refran_completo)
        #print('\n'.join(refranes))
        

   
#proceso3 divide autor y cita para mostrarlo por pantalla separado por un :
def proceso3(cola2):
    with open('Ejercicio1/refranes.txt', 'w') as f:
        while True:
            linea = cola2.get()
            if linea is None:
                break
            refran1 = linea.rsplit(';',1)
            autor=linea.rsplit(';',2)
            refran_completo, _ = linea.strip()
            print(autor+" : "+refran1 + '\n')
            
    
def main():
    categoria = str(input("Introduce una categoría:"))
    
    
    ruta_fichero = "Ejercicio1/refranes.txt"
    try:
        with open(ruta_fichero, 'r'):
            pass
    except FileNotFoundError:
        print("El fichero no existe.")
        return

    output_queue = Queue()
    cola2=Queue()

    # Proceso 1
    p1 = Process(target=proceso1, args=(ruta_fichero, categoria, output_queue))
    p1.start()
    p1.join()

    # Proceso 2
    p2 = Process(target=proceso2, args=(output_queue,cola2))
    p2.start()
    p2.join()

    #proceso3
    p3= Process(target=proceso3,args=(cola2))
    p3.start()
if __name__ == "__main__":
    main()
  