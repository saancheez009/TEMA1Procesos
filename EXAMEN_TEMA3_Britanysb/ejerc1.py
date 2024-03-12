import threading
import random
import time

# Definir semáforos
mutex_maquinas = threading.Semaphore(2)  # Dos máquinas disponibles
mutex_dependientes = threading.Semaphore(5)  # Cinco dependientes disponibles

def cliente(nombre):
    print(f"{nombre} llega a la hamburguesería.")
    time.sleep(random.randint(1, 4))  # Tiempo para sacar el ticket

    print(f"{nombre} espera a que una máquina esté libre.")
    mutex_maquinas.acquire()
    print(f"{nombre} está sacando un ticket.")

    time.sleep(random.randint(3, 7))  # Tiempo para ser atendido en el mostrador
    print(f"{nombre} espera a ser atendido por un dependiente.")
    mutex_dependientes.acquire()
    print(f"{nombre} está siendo atendido.")

    # Simular proceso de obtener la comida
    time.sleep(2)
    print(f"{nombre} ha conseguido su comida y se va.")
    mutex_dependientes.release()
    mutex_maquinas.release()

# Crear hilos de clientes
clientes = []
for i in range(10):
    nombre_cliente = f"Cliente {i+1}"
    cliente_thread = threading.Thread(target=cliente, args=(nombre_cliente,))
    clientes.append(cliente_thread)

# Iniciar los hilos de los clientes
for cliente_thread in clientes:
    cliente_thread.start()

# Esperar a que todos los clientes terminen
for cliente_thread in clientes:
    cliente_thread.join()

print("Todos los clientes han sido atendidos.")