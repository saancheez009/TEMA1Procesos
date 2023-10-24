"""Crea un programa que pida diez números reales por teclado,
los almacene en una lista, y luego lo recorra para averiguar el máximo
y mínimo y mostrarlos por pantalla."""

numeros=[]

for i in range (10):
    
    numero = int(input("Por favor introduzca 10 números reales"))

    numeros.append(numero)

# Inicializamos las variables para almacenar el máximo y el mínimo
maximo = numeros[0]
minimo = numeros[0]

# Recorremos la lista para encontrar el máximo y el mínimo
for numero in numeros:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

# Mostramos el resultado por pantalla
print("El número máximo es:", maximo)
print("El número mínimo es:", minimo)


2 / 2





