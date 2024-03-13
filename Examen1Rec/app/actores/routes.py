from flask import Blueprint, request

from utils.functions import escribeFichero, leeFichero

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

@actoresBP.post('/')
def agregarActor():
    nuevo_actor = request.json
    actores = leeFichero(rutaActores)
    
    if "PeliculaId" not in nuevo_actor:
        return {"error": "Falta el campo PeliculaId en el nuevo actor"}, 400
    
    # Verifica si el PeliculaId existe en la lista de películas
    peliculas = leeFichero(rutaPeliculas)
    if not any(pelicula["id"] == nuevo_actor["PeliculaId"] for pelicula in peliculas):
        return {"error": "El id de la pelicula no existe en la lista de películas"}, 404
    
    actores.append(nuevo_actor)
    escribeFichero(rutaActores, actores)
    return nuevo_actor, 201

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