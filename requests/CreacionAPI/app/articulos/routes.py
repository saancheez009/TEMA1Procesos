from utils.functions import *

from flask import Blueprint, jsonify

rutaFichero = "proyecto/ficheros/articulos.json"
articulosBP = Blueprint('articulos', __name__)

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