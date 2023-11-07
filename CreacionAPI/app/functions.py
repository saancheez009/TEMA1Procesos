import json

def leeFichero(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    try:
        data = json.load(archivo)
        archivo.close()
        return data
    except json.JSONDecodeError:
        return[]

def escribeFichero(nombreArchivo, data):
    archivo = open(nombreArchivo, "w")
    json.dump(data, archivo)
    archivo.close()
