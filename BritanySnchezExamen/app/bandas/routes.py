from flask import Flask,Blueprint,jsonify,request
from flask_jwt_extended import jwt_required

from app.utils.functions import escribeFichero, leeFichero 

app=Flask(__name__)

rutaFichero="app\ficheros\bandas.json"
bandasBP = Blueprint('bandas',__name__)

def find_next_id():
    bandas=leeFichero()
    return max(banda["id"] for banda in bandas)+1


@bandasBP.get('/')
def get_bandas():
    bandas = leeFichero(rutaFichero)
    return jsonify(bandas)

@bandasBP.get("/<int:id>")
def  get_banda(id):
    bandas= leeFichero(rutaFichero)
    for banda in bandas:
        if banda['id']==id:
            return banda,200

    return {"error":"Banda not found "},404

@bandasBP.post('/')
@jwt_required()
def añadir_banda():
    bandas=leeFichero(rutaFichero)
    
    if request.is_json:
        banda = request.get_json()
        
        banda["id"]= find_next_id()
        bandas.append(banda)
        escribeFichero(bandas)
        return banda,201
    return {"error":"Request must be JSON"},415

@bandasBP.put("/<int:id>")
@bandasBP.patch("/<int:id>")
@jwt_required()
def modificar_banda(id):
    bandas=leeFichero(rutaFichero)
    if request.is_json:
        newBanda=request.get_json()
        
        for banda in bandas:
            if banda["id"]==id:
                for element in newBanda:
                    banda[element]= newBanda[element]
                    
                return banda,200
    return {"error":"Requests must be JSON"},415 

@bandasBP.delete("/<int:id>")
@jwt_required()
def borrar_banda(id):
    bandas=leeFichero(rutaFichero)
    for banda in bandas:
        if banda['id']== id:
            bandas.remove(banda)
            return "{}",200
    return {"error": "Banda not found"},404