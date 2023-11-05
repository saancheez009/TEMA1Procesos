
from app.funciones.functions import *

from flask import Blueprint, jsonify, request



ficheroPeriodistas = "ficheros/periodistas.json"
ficheroArticulos = "ficheros/articulos.json"

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
def get_periodista(id):
    periodistas = leeFichero(ficheroPeriodistas)
    for periodista in periodistas:
        if periodista['id'] == id:
            return periodista, 200
    return {"error": "Periodista no encontrado"}, 404


@periodistasBP.post("/")

def add_periodista():
    periodistas = leeFichero(ficheroPeriodistas)

    if request.is_json:
     
        periodista = request.get_json()
     
        periodista["id"] = find_next_id()
      
        periodistas.append(periodista)
        escribeFichero(ficheroPeriodistas, periodistas)
        
        return periodista, 201
    
    return {"error": "Request must be JSON"}, 415

@periodistasBP.put("/<int:id>")
@periodistasBP.patch("/<int:id>")

def modify_country(id):
    periodistas = leeFichero(ficheroPeriodistas)
   
    if request.is_json:
       
        nuevoPeriodista = request.get_json()
       
        for periodista in periodistas:
            if periodista["id"] == id:
                
                for element in nuevoPeriodista:
                    periodista[element] = nuevoPeriodista[element]
                escribeFichero(ficheroPeriodistas, periodistas)
               
                return periodista, 200
  
    return {"error": "Request must be JSON"}, 415

@periodistasBP.delete("/<int:id>")

def delete_periodista(id):
    periodistas = leeFichero(ficheroPeriodistas)
  
    for periodista in periodistas:
        if periodista['id'] == id:
            periodistas.remove(periodista)
            escribeFichero(ficheroPeriodistas, periodistas)
            
            return {}, 200

    return {"error": "Periodista no encontrado"}, 404

@periodistasBP.get("/<int:id>/articulos")
def get_articulos(id):
    list = []
    articulos = leeFichero(ficheroArticulos)
    for articulo in articulos:
        if articulo['articulosId'] == id:
            list.append(articulo)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No hay artículos encontrados para este periodista"}, 404