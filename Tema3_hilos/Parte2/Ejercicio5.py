import threading
import time
import random

# Libros disponibles
libros_disponibles = list(range(1, 10))

# Presta libros
def prestamo(nombre_estudiante):
    global libros_disponibles

    # Selecciona dos libros al azar
    libros_seleccionados = random.sample(libros_disponibles, 2)

    while not all(libro in libros_disponibles for libro in libros_seleccionados):
        time.sleep(1)  

    with threading.Lock():
        print(f"{nombre_estudiante} ha tomado los libros {libros_seleccionados[0]} y {libros_seleccionados[1]}.")

    # Utiliza los libros durante un tiempo aleatorio entre 3 y 5 segundos
    tiempo_uso = random.uniform(3, 5)
    time.sleep(tiempo_uso)

    #Devuelve los libros
    with threading.Lock():
        print(f"{nombre_estudiante} ha devuelto los libros {libros_seleccionados[0]} y {libros_seleccionados[1]}.")
        libros_disponibles.extend(libros_seleccionados)


if __name__ == "__main__":
    estudiantes = []

    for i in range(4):
        nombre_estudiante = f"Estudiante{i+1}"
        estudiante = threading.Thread(target=prestamo, args=(nombre_estudiante,))
        estudiantes.append(estudiante)
        estudiante.start()

    for estudiante in estudiantes:
        estudiante.join()