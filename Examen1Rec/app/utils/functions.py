import ficheros
import json

def leeFichero(rutaFichero):
    try:
        archivo=open(rutaFichero,"r")
        data = json.load(archivo) #coge datos de un archivo que esta en modo json
    except json.JSONDecodeError:
        data=[]
    archivo.close()
    return data

def escribeFichero(lista,rutaFichero):
    archivo = open(rutaFichero, "w")
    json.dump(lista, archivo)
    archivo.close()
    
def nuevo_id(lista):
    return max(i ["id"] for i in lista)+1
