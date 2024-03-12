import threading
import random
import time

# Constantes
NUM_VOLUNTARIOS = 4
NUM_GESTORES = 4
LIMITE_RECAUDACION = 2000

# Definir semáforos
mutex_recaudacion = threading.Semaphore(1)  # Controla acceso a la recaudación
voluntarios_esperando = threading.Semaphore(0)  # Voluntarios esperando si se supera el límite
gestores_esperando = threading.Semaphore(0)  # Gestores esperando si no hay suficiente dinero

recaudacion = 0  # Inicialmente no hay dinero recaudado

def voluntario(nombre):
    global recaudacion
    while True:
        dinero_recaudado = random.randint(4, 25)
        tiempo_recaudacion = random.randint(1, 3)
        
        time.sleep(tiempo_recaudacion)
        
        mutex_recaudacion.acquire()
        if recaudacion + dinero_recaudado > LIMITE_RECAUDACION:
            print(f"{nombre} espera a que haya espacio suficiente para añadir {dinero_recaudado}€.")
            mutex_recaudacion.release()
            voluntarios_esperando.acquire()
        else:
            recaudacion += dinero_recaudado
            print(f"{nombre} aporta {dinero_recaudado}€. Total recaudado: {recaudacion}€.")
            if recaudacion >= LIMITE_RECAUDACION:
                print(f"¡Se ha superado el límite de {LIMITE_RECAUDACION}€!")
                voluntarios_esperando.release()
            mutex_recaudacion.release()

def gestor(nombre):
    global recaudacion
    while True:
        dinero_retirado = random.randint(10, 40)
        tiempo_retirada = random.randint(2, 5)
        
        time.sleep(tiempo_retirada)
        
        mutex_recaudacion.acquire()
        if recaudacion < dinero_retirado:
            print(f"{nombre} espera a que haya suficiente dinero para retirar {dinero_retirado}€.")
            mutex_recaudacion.release()
            gestores_esperando.acquire()
        else:
            recaudacion -= dinero_retirado
            print(f"{nombre} retira {dinero_retirado}€. Dinero restante: {recaudacion}€.")
            if recaudacion < LIMITE_RECAUDACION:
                voluntarios_esperando.release()
            mutex_recaudacion.release()

# Crear hilos de voluntarios
hilos_voluntarios = []
for i in range(NUM_VOLUNTARIOS):
    nombre_voluntario = f"Voluntario {i+1}"
    hilo_voluntario = threading.Thread(target=voluntario, args=(nombre_voluntario,))
    hilos_voluntarios.append(hilo_voluntario)

# Crear hilos de gestores
hilos_gestores = []
for i in range(NUM_GESTORES):
    nombre_gestor = f"Gestor {i+1}"
    hilo_gestor = threading.Thread(target=gestor, args=(nombre_gestor,))
    hilos_gestores.append(hilo_gestor)

# Iniciar los hilos de voluntarios
for hilo_voluntario in hilos_voluntarios:
    hilo_voluntario.start()

# Iniciar los hilos de gestores
for hilo_gestor in hilos_gestores:
    hilo_gestor.start()