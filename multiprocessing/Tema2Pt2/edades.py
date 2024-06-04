from multiprocessing import Process, Queue

def proceso1(ruta, year, output_queue):
    with open(ruta, 'r') as file:
        lines = file.readlines()
        movies_in_year = [line.strip() for line in lines if line.split(';')[-1].strip() == str(year)]
        output_queue.put(movies_in_year)

def proceso2(output_queue):
    movies = []
    while not output_queue.empty():
        movies.extend(output_queue.get())
    
    if movies:
        year = movies[0].split(';')[-1].strip()
        output_filename = f'peliculas{year}.txt'
        with open(output_filename, 'w') as output_file:
            output_file.write('\n'.join(movies))
        print(f'Películas almacenadas en el archivo {output_filename}')

def main():
    year = int(input("Introduce un año (menor al actual): "))
    if year >= 2023: 
        print("El año debe ser menor al actual.")
        return
    
    ruta_fichero = "Tema2Pt2/pelis.txt"
    try:
        with open(ruta_fichero, 'r'):
            pass
    except FileNotFoundError:
        print("El fichero no existe.")
        return

    output_queue = Queue()

    # Proceso 1
    p1 = Process(target=proceso1, args=(ruta_fichero, year, output_queue))
    p1.start()
    p1.join()

    # Proceso 2
    p2 = Process(target=proceso2, args=(output_queue,))
    p2.start()
    p2.join()

if __name__ == "__main__":
    main()

#

from multiprocessing import Process
import random

def proceso1(nombreArchivo):
    with open(nombreArchivo, "w") as archivo:
        for i in range(6):
            nota = round(random.uniform(1,10), 2) 
            archivo.write(str(nota)+"\n")

def proceso2(nombreArchivo, nombreAlumno):
    suma = 0
    with open(nombreArchivo, "r") as archivo:
        for notaCadena in archivo.readlines():
            suma += float(notaCadena)
    
    media = round(suma/6,2)

    with open("medias.txt", "a") as archivo:
        archivo.write(str(media) + " " + nombreAlumno + "\n")

def proceso3():
    max = 0
    alumnoMax = ""
    with open("medias.txt", "r") as archivo:
        for linea in archivo.readlines():
            datos = linea.split(" ")
            nota = float(datos[0])
            alumno = datos[1]
            if nota > max:
                max = nota
                alumnoMax = alumno
    print("Nota máxima", max, alumnoMax)

if __name__ == "__main__":
    lista = []

    for i in range(1,11):
        p1 = Process(target=proceso1, args=(f"alumno{i}.txt",))
        p1.start()
        lista.append(p1)

    for proceso in lista:
        proceso.join()

    lista = []
    for i in range(1,11):
        p2 = Process(target=proceso2, args=(f"alumno{i}.txt", f"alumno{i}"))
        p2.start()
        lista.append(p2)

    for proceso in lista:
        proceso.join()
    
    p3 = Process(target=proceso3)
    p3.start()
    

    p3.join()


    #nombres
    import multiprocessing
import os
from datetime import datetime

# Proceso 1: Filtrar alumnos según la edad
def proceso_1(edad, cola_1):
    año_actual = datetime.now().year
    with open('PSEP.txt', 'r') as f:
        for linea in f:
            linea = linea.strip()
            nombre_completo, año_nacimiento = linea.rsplit(' -', 1)
            año_nacimiento = int(año_nacimiento)
            edad_alumno = año_actual - año_nacimiento
            if edad_alumno > edad:
                cola_1.put(linea)
    cola_1.put(None)  # Indicar que ya no hay más alumnos

# Proceso 2: Extraer nombres y apellidos
def proceso_2(cola_1, cola_2):
    while True:
        linea = cola_1.get()
        if linea is None:
            cola_2.put(None)
            break
        nombre_completo, _ = linea.rsplit(' -', 1)
        cola_2.put(nombre_completo)

# Proceso 3: Escribir en fichero
def proceso_3(cola_2):
    with open('alumnado.txt', 'w') as f:
        while True:
            linea = cola_2.get()
            if linea is None:
                break
            nombre_completo = linea.strip()
            f.write(nombre_completo + '\n')

# Main
def main():
    try:
        edad = int(input("Introduce una edad: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        return

    cola_1 = multiprocessing.Queue()
    cola_2 = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=proceso_1, args=(edad, cola_1))
    p2 = multiprocessing.Process(target=proceso_2, args=(cola_1, cola_2))
    p3 = multiprocessing.Process(target=proceso_3, args=(cola_2,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("El proceso ha finalizado. Revisa el archivo 'alumnado.txt'.")

if __name__ == "__main__":
    main()







import multiprocessing
import random
import os

# Proceso 1: Generar edades
def generar_edades(aula):
    filename = f'edades{aula:02d}.txt'
    with open(filename, 'w') as f:
        edades = [random.randint(18, 99) for _ in range(30)]
        for edad in edades:
            f.write(f"{edad}\n")

# Proceso 2: Generar alturas
def generar_alturas(aula):
    filename = f'alturas{aula:02d}.txt'
    with open(filename, 'w') as f:
        alturas = [round(random.uniform(1, 2), 2) for _ in range(30)]
        for altura in alturas:
            f.write(f"{altura}\n")

# Proceso 3: Calcular media de edades
def calcular_media_edades(aula, queue):
    filename = f'edades{aula:02d}.txt'
    try:
        with open(filename, 'r') as f:
            edades = [int(line.strip()) for line in f]
            media = sum(edades) / len(edades)
            queue.put(media)
    except FileNotFoundError:
        print(f"El fichero {filename} no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el fichero {filename}: {e}")

# Proceso 4: Calcular media de alturas
def calcular_media_alturas(aula, queue):
    filename = f'alturas{aula:02d}.txt'
    try:
        with open(filename, 'r') as f:
            alturas = [float(line.strip()) for line in f]
            media = sum(alturas) / len(alturas)
            queue.put(media)
    except FileNotFoundError:
        print(f"El fichero {filename} no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el fichero {filename}: {e}")

# Main
def main():
    num_aulas = 20

    # Eliminar archivos anteriores
    for i in range(1, num_aulas + 1):
        try:
            os.remove(f'edades{i:02d}.txt')
        except FileNotFoundError:
            pass
        try:
            os.remove(f'alturas{i:02d}.txt')
        except FileNotFoundError:
            pass
    try:
        os.remove('media_edades.txt')
    except FileNotFoundError:
        pass
    try:
        os.remove('media_alturas.txt')
    except FileNotFoundError:
        pass

    # Generar edades y alturas para 20 aulas
    procesos = []
    for i in range(1, num_aulas + 1):
        p1 = multiprocessing.Process(target=generar_edades, args=(i,))
        p2 = multiprocessing.Process(target=generar_alturas, args=(i,))
        procesos.append(p1)
        procesos.append(p2)
        p1.start()
        p2.start()

    for p in procesos:
        p.join()

    # Calcular medias de edades y alturas
    queue_edades = multiprocessing.Queue()
    queue_alturas = multiprocessing.Queue()

    procesos = []
    for i in range(1, num_aulas + 1):
        p3 = multiprocessing.Process(target=calcular_media_edades, args=(i, queue_edades))
        p4 = multiprocessing.Process(target=calcular_media_alturas, args=(i, queue_alturas))
        procesos.append(p3)
        procesos.append(p4)
        p3.start()
        p4.start()

    for p in procesos:
        p.join()

    # Recoger resultados de las colas y calcular medias totales
    medias_edades = []
    medias_alturas = []

    while not queue_edades.empty():
        medias_edades.append(queue_edades.get())

    while not queue_alturas.empty():
        medias_alturas.append(queue_alturas.get())

    media_total_edades = sum(medias_edades) / len(medias_edades) if medias_edades else 0
    media_total_alturas = sum(medias_alturas) / len(medias_alturas) if medias_alturas else 0

    with open('media_edades.txt', 'w') as f:
        f.write(f"Media de edades de todas las aulas: {media_total_edades}\n")

    with open('media_alturas.txt', 'w') as f:
        f.write(f"Media de alturas de todas las aulas: {media_total_alturas}\n")

    print("Se han generado los archivos y calculado las medias.")

if __name__ == "__main__":
    main()
    