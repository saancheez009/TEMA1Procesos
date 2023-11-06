from app.functions import *

from flask import Blueprint, jsonify, request

rutaFichero = "ficheros/articulos.json"
articulosBP = Blueprint('articulos', __name__)

def find_next_id():
    articulos = leeFichero(rutaFichero)
    max = articulos[0]["id"]
    for articulo in articulos:
        if articulo["id"] > max:
            max = articulo["id"]

    return max+1
@articulosBP.get('/')
def get_articulos():
    articulos = leeFichero(rutaFichero)
    return jsonify(articulos)

@articulosBP.get("/<int:id>")
def get_articulo(id):
    articulos = leeFichero(rutaFichero)
    for articulo in articulos:
        if articulo['id'] == id:
            return articulo, 200
    return {"error": "Artículo no encontrado"}, 404

@articulosBP.post("/")

def add_articulo():
    articulos = leeFichero(rutaFichero)

    if request.is_json:
     
        articulo = request.get_json()
     
        articulo["id"] = find_next_id()
      
        articulos.append(articulo)
        escribeFichero(rutaFichero, articulos)
        
        return articulo, 201
    
    return {"error": "Request must be JSON"}, 415

@articulosBP.put("/<int:id>")
@articulosBP.patch("/<int:id>")

def modify_country(id):
    articulos = leeFichero(rutaFichero)
   
    if request.is_json:
       
        nuevoArticulo = request.get_json()
       
        for articulo in articulos:
            if articulo["id"] == id:
                
                for element in nuevoArticulo:
                    articulo[element] = nuevoArticulo[element]
                escribeFichero(rutaFichero, articulos)
               
                return articulo, 200
  
    return {"error": "Request must be JSON"}, 415

@articulosBP.delete("/<int:id>")

def delete_articulo(id):
    articulos = leeFichero(rutaFichero)
  
    for articulo in articulos:
        if articulo['id'] == id:
            articulos.remove(articulo)
            escribeFichero(rutaFichero, articulos)
            
            return {}, 200

    return {"error": "Artículo no encontrado"}, 404