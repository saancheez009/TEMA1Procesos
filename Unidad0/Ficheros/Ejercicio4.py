file = open("numeros.txt","rt", encoding="utf8")
lista = []
for linea in file.readlines():
    num= int(linea)
    lista.append(num)

print(lista)
lista.sort()
file.close()


fileEscritura = open("numeros_ordenados.txt","w", encoding="utf8")

for numero in lista:
    fileEscritura.write(str(numero) + "\n")

fileEscritura.close()