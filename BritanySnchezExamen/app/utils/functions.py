import json

import requests



def leeFichero():
    archivo = open("database.json","r")
    bandas = json.load(archivo)
    archivo.close()
    return bandas

def escribeFichero(bandas):
    archivo = open("database.json", "w")
    json.dump(bandas,archivo)
    archivo.close
    
def create_access_token():
    api_url=""
    token ="jfhuuhf"
    header={"Authorization":F"Bearer{token}"}
    response= requests.get(api_url, headers=header)