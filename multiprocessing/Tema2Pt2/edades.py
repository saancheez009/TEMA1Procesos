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
    