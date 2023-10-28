
from utils.functions import *

from flask import Blueprint, jsonify, request

ficheroPeriodistas = "../proyecto/ficheros/periodistas.json"
ficheroAtriculos = "../proyecto/ficheros/articulos.json"

periodistasBP = Blueprint('periodistas', __name__)

def find_next_id():
    periodistas = leeFichero(ficheroPeriodistas)
    max = periodistas[0]["id"]
    for periodista in periodistas:
        if periodista["id"] > max:
            max = periodista["id"]

    return max+1

@periodistasBP.get('/')
def get_periodistas():
    periodistas = leeFichero(ficheroPeriodistas)
    return jsonify(periodistas)

@periodistasBP.get("/<int:id>")
def get_country(id):
    periodistas = leeFichero(ficheroPeriodistas)
    for periodista in periodistas:
        if periodista['id'] == id:
            return periodista, 200
    return {"error": "Periodista no encontrado"}, 404


@periodistasBP.post("/")

def add_country():
    periodistas = leeFichero(ficheroPeriodistas)
    # Comprobamos si la petición cumple con el formato json
    if request.is_json:
        # Guardamos el formato JSON
        periodista = request.get_json()
        # Le asignamos un nuevo id
        periodista["id"] = find_next_id()
        # Añadimos el nuevo periodista a nuestra lista
        periodistas.append(periodista)
        escribeFichero(ficheroPeriodistas, periodistas)
        # Devolvemos al periodista en formato diccionario y 201
        return periodista, 201
    # Si la petición no cumple con el formato JSON
    return {"error": "Request must be JSON"}, 415

@periodistasBP.put("/<int:id>")
@periodistasBP.patch("/<int:id>")
# definimos la función correspondiente
def modify_country(id):
    periodistas = leeFichero(ficheroPeriodistas)
    # Se comprueba si la petición que nos ha llegado cumple con el formato json
    if request.is_json:
       
        nuevoPeriodista = request.get_json()
       
        for periodista in periodistas:
            if periodista["id"] == id:
                
                for element in nuevoPeriodista:
                    periodista[element] = nuevoPeriodista[element]
                escribeFichero(ficheroPeriodistas, periodistas)
               
                return periodista, 200
    # Si la petición no cumple con el formato JSON devuelve un mensaje de error y el código 415
    return {"error": "Request must be JSON"}, 415

@periodistasBP.delete("/<int:id>")
# Se debe añadir como parámetro de entrada el id que se 
# indica en la dirección
def delete_periodista(id):
    periodistas = leeFichero(ficheroPeriodistas)
  
    for periodista in periodistas:
        if periodista['id'] == id:
            periodistas.remove(periodista)
            escribeFichero(ficheroPeriodistas, periodistas)
            
            return {}, 200
    # Si no se encuentra, se devuelve mensaje de error y código 404
    return {"error": "Periodista no encontrado"}, 404

@periodistasBP.get("/<int:id>/articulo")
def get_periodistas(id):
    list = []
    articulos = leeFichero(ficheroPeriodistas)
    for articulo in articulos:
        if articulo['articuloId'] == id:
            list.append(articulo)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No hay artículos encontrados para este periodista"}, 404