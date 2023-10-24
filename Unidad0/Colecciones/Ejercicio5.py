"""Crea un programa que cree una lista de enteros de tamaño 100 y lo rellene con valores enteros aleatorios entre 1 y 10 
(utiliza 1 + Math.random()*10). Luego pedirá un valor N y
mostrará cuántas veces aparece N. 
"""

import random

# Crear una lista de enteros aleatorios entre 1 y 10

lista_enteros = [random.randint(1, 10) for _ in range(100)]

# Solicitar al usuario un valor N
num = int(input("Ingresa un valor N para buscar en la lista: "))

# Contar cuántas veces aparece N en la lista
contador = lista_enteros.count(num)

# Mostrar el resultado
print(f"El valor {num} aparece {contador} veces en la lista.")