from multiprocessing import Process
import random

#Proceso1 , genera las puntuaciones de forma aleatoria 
def proceso1(nombreArchivo):
    with open(nombreArchivo, "w") as archivo:
        #se generan 10 puntuaciones para cada jugador
        for i in range(10):
            #las puntuaciones van de 0 a 100
            puntuacion = (random.randint(0,100)) 
            #se escriben las 10 puntuaciones en el fichero de cada jugador
            archivo.write(str(puntuacion)+"\n")

#Proceso2 recibe el nombre del archivo de cada jugador y el nombre de cada jugador para calcular su puntuación total
def proceso2(nombreArchivo, jugadornombre):
    suma=0
    #Se lee cada archivo y realiza la suma de todas las puntuaciones de cada jugador
    with open(nombreArchivo, "r") as archivo:
        for puntuacionCadena in archivo.readlines():
            suma += float(puntuacionCadena)
    
#se genera un fichero con el total de puntuaciones de cada jugador
    with open("total_puntuaciones.txt", "a") as archivo:
        archivo.write(str(suma) + " " + jugadornombre + "\n")

#En este proceso se calcula la puntuación máxima
def proceso3():
    max=0
    max_puntuacion=" "
    with open("total_puntuaciones.txt", "r") as archivo:
        for linea in archivo.readlines():
            datos = linea.split(" ")
            puntuaciones = float(datos[0])
            jugador = datos[1]
            if puntuaciones > max:
                max = puntuaciones
                max_puntuacion   = jugador
    print("Puntuación máxima", max, max_puntuacion)

if __name__ == "__main__":
    lista = []
#se crean 20 ficheros, 1 para cada jugador, en este caso son 20 jugadores
    for i in range(1,21):
        p1 = Process(target=proceso1, args=(f"jugador{i}.txt",))
        p1.start()
        lista.append(p1)
#Finaliza el proceso
    for proceso in lista:
        proceso.join()

    lista = []
    #se recorren los 20 ficheros de los jugadores para calcular sus puntuaciones totales
    for i in range(1,21):
        #se le pasa el nombre del jugador y el nombre del fichero
        p2 = Process(target=proceso2, args=(f"jugador{i}.txt", f"jugador{i}"))
        p2.start()
        lista.append(p2)
#Finaliza el proceso
    for proceso in lista:
        proceso.join()
   
    p3 = Process(target=proceso3)
    p3.start()
    #finaliza el proceso
    p3.join()
    