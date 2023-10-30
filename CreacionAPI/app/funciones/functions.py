import json

def leeFichero(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    data = json.load(archivo)
    archivo.close()
    return data

def escribeFichero(nombreArchivo, data):
    archivo = open(nombreArchivo, "w")
    json.dump(data, archivo)
    archivo.close()
