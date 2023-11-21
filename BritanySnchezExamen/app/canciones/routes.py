from flask import Blueprint, Flask,jsonify, request
from flask_jwt_extended import jwt_required


from app.utils.functions import *

app=Flask(__name__)

rutaFichero="app/ficheros/canciones.json"
cancionesBP= Blueprint('canciones',__name__)

def find_next_id():
    canciones=leeFichero(rutaFichero)
    return max(cancion["id"] for cancion in canciones)+1

@cancionesBP.get('/')
def get_canciones():
    canciones=leeFichero(rutaFichero)
    return jsonify(canciones)

@cancionesBP.get("/<int:id>")
def get_cancion(id):
    canciones=leeFichero(rutaFichero)
    for cancion in canciones:
        if cancion['id']==id:
            return cancion,200
    return {"error":"Song not found"},404

@cancionesBP.post('/')
@jwt_required()
def añadir_cancion():
    canciones=leeFichero(rutaFichero)
    
    if request.is_json:
        cancion = request.get_json()
        
        cancion["id"]= find_next_id()
        canciones.append(cancion)
        escribeFichero(canciones)
        return cancion,201
    return {"error":"Request must be JSON"},415


@cancionesBP.put("/<int:id>")
@cancionesBP.patch("/<int:id>")
@jwt_required()

def modificar_cancion(id):
    canciones=leeFichero(rutaFichero)
    if request.is_json:
        newCancion=request.get_json()
        
        for cancion in canciones:
            if cancion["id"]==id:
                for element in newCancion:
                    cancion[element]= newCancion[element]
                    
                return cancion,200
    return {"error":"Requests must be JSON"},415 

@cancionesBP.delete("/<int:id>")
@jwt_required()

def borrar_cancion(id):
    canciones=leeFichero(rutaFichero)
    for cancion in canciones:
        if cancion['id']== id:
            canciones.remove(cancion)
            return "{}",200
    return {"error": "Song not found"},404