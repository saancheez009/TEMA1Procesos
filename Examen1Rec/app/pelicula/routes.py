from flask import Blueprint

from utils.functions import *

rutaPeliculas="app/ficheros/peliculas.json"
peliculasBP = Blueprint('peliculas', __name__)

@peliculasBP.get('/<int:id_pelicula>')
def getPelicula(id_pelicula):
    peliculas = leeFichero(rutaPeliculas)
    
    for pelicula in peliculas:
        if pelicula["id"]== id_pelicula:
            return pelicula,200
    return{"error" : "Pelicula no encontrada"},404