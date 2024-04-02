from flask import Blueprint, request
from bcrypt import *
from flask_jwt_extended import create_access_token
from utils.functions import*
usersBP=Blueprint('users',__name__)

rutaUsuarios ="app/ficheros/users.json"
@usersBP.post('/')
def registerUser():
    listaUsuarios = leeFichero(rutaUsuarios)
    
    if request.is_json:
        nuevoUsuario = request.get_json()
        contransenya = nuevoUsuario["password"].encode("UTF-8")
        sal = gensalt()
        hash=hashpw(contransenya,sal).hex()
        nuevoUsuario["password"] = hash
        listaUsuarios.append(nuevoUsuario)
        escribeFichero(listaUsuarios,rutaUsuarios)
        return nuevoUsuario,201
    
    else:
        return{"error": "JSON no correcto"},415
    
@usersBP.get('/')
def loginUser():
    usuarios=leeFichero(rutaUsuarios)
    if request.is_json:
        usuarioJSON = request.get_json() #{"username": "britany", "password":"1234"}
        nombreUsuario =usuarioJSON["username"]
        
        for usuario in usuarios:
            if usuario["username"]==nombreUsuario:
                contrasenyaJSON=usuarioJSON["password"].encode("UTF-8")
                if checkpw(contrasenyaJSON, bytes.fromhex(usuario["password"])):
                    #autenticacioN correcta
                    token=create_access_token(identity=nombreUsuario)
                    return {'token' : token},200
                
                else:
                    return{"error": "No autorizado"},401
                
        return{"error": "usuario no encontrado"},404
    return{"error":"JSON no es correcto"},415