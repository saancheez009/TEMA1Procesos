from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from utils.functions import *
rutaActores="app/ficheros/actores.json"
rutaPeliculas="app/ficheros/peliculas.json"
peliculasBP = Blueprint('peliculas', __name__)

@peliculasBP.get('/<int:id_pelicula>')
def getPelicula(id_pelicula):
    peliculas = leeFichero(rutaPeliculas)
    
    for pelicula in peliculas:
        if pelicula["id"]== id_pelicula:
            return pelicula,200
    return{"error" : "Pelicula no encontrada"},404

# Método GET para obtener una película con la lista de actores
@peliculasBP.get('/<int:id_pelicula>/actores')
def getPeliculaConActores(id_pelicula):
    actores = leeFichero(rutaActores)
    lista=[]
    
    for actor in actores:
        if actor["idPelicula"]==id_pelicula:
            lista.append(actor)
    if len(lista)>0:
        return lista,200
    return {"error": "no hay actores para la pelicula"},404

   # for pelicula in peliculas:
   #     if pelicula["id"] == id_pelicula:
   #         actores_pelicula = [actor for actor in actores if actor["idPelicula"] == id_pelicula]
   #         if actores_pelicula:
   #             pelicula["actores"] = actores_pelicula
   #             return pelicula, 200
   #         else:
   #             return {"error": "No hay actores para esta película"}, 404

   #     return {"error": "Pelicula no encontrada"}, 404
   
   #Si el ID que se intenta modificar no existe, se debe añadir un nuevo recurso con los datos pasados en el JSON. Si existe, se modifican los datos indicados en el JSON.
    
@peliculasBP.put('/<int:id_pelicula>')
@jwt_required()
def modificarPelicula(id_pelicula):
    peliculas = leeFichero(rutaPeliculas)
    if request.is_json: 
        nueva_pelicula = request.get_json()

        for pelicula in peliculas:
            if pelicula["id"] == id_pelicula:
                pelicula.update(nueva_pelicula)  # Modifica los datos existentes con los datos proporcionados en el JSON
                escribeFichero(rutaPeliculas, peliculas)
                return pelicula, 200
        
        # Si el ID no existe, añadir un nuevo recurso con los datos pasados en el JSON
        nueva_pelicula["id"] = id_pelicula
        peliculas.append(nueva_pelicula)
        escribeFichero(rutaPeliculas, peliculas)
        return nueva_pelicula, 201
    else:
        return {"error":"JSON erróneo"},415