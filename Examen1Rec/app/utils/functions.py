import json

def leeFichero(rutaFichero):
    archivo=open(rutaFichero,"r")
    data = json.load(archivo) #coge datos de un archivo que esta en modo json
    archivo.close()
    return data

def escribeFichero(rutaFichero, lista):
    archivo = open(rutaFichero, "w")
    json.dump(lista, rutaFichero)
    archivo.close()
