from flask import Blueprint, jsonify, request
from utils.functions import *

actoresBP = Blueprint('actores',__name__)
rutaActores="app/ficheros/actores.json"
rutaPeliculas="app/ficheros/peliculas.json"

@actoresBP.get('/<int:id_actor>')
def getActor(id_actor):
    actores = leeFichero(rutaActores)
    
    for actor in actores:
        if actor["id"]== id_actor:
            return actor,200
    return{"error" : "Actor no encontrado"},404

@actoresBP.get('/')
def getActores():
    actores=leeFichero(rutaActores)
    return jsonify(actores),200

@actoresBP.post('/')
def agregarActor():
    if request.is_json:
        actores = leeFichero(rutaActores)
        peliculas=leeFichero(rutaPeliculas)
        nuevo_actor=request.get_json()
        for pelicula in peliculas:
            if pelicula["id"]==nuevo_actor["idPelicula"]:
                nuevo_actor["id"]=nuevo_id(actores)
                actores.append(nuevo_actor)
                escribeFichero(rutaActores, actores)
                return nuevo_actor,201
                #se añadirá el actor ala lista de actores
                #calcular nuevo id
        return {"error": "La pelicula no existe"},404
    return {"error": "JSON no correcto"},415



# Método DELETE para eliminar un actor por su ID
@actoresBP.delete('/<int:id_actor>')
def eliminarActor(id_actor):
    actores = leeFichero(rutaActores)
    
    for actor in actores:
        if actor["id"] == id_actor:
            actores.remove(actor)
            escribeFichero(rutaActores, actores)
            return {"mensaje": "Actor eliminado correctamente"}, 200
    
    return {"error": "Actor no encontrado"}, 404