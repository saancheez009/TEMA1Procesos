"""Realiza un programa que pida 8 números enteros y los almacene en una
lista. A continuación, recorrerá esa tabla y mostrará esos números junto
con la palabra “par” o “impar” según proceda.
"""

numeros=[]

for i in range(8):
    num=int(input("Porfavor introduzca 8 números enteros: "))

    numeros.append(num)

for num in numeros:
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")


