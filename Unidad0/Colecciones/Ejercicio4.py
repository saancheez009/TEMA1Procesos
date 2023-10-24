"""Escribe un programa que lea 10 números por teclado y que luego los 
muestre ordenados de mayor a menor.
"""

numeros=[]

for i in range (10):
    numero=int(input("Por favor introduzca 10 números: "))
    numeros.append(numero)

numeros.sort(reverse=True)
print(numeros)