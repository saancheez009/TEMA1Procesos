from app.functions import *
import bcrypt
from flask_jwt_extended import create_access_token


from flask import Blueprint, request

ficheroUsers = "ficheros/users.json"

usersBP = Blueprint('users', __name__)


@usersBP.post('/')
def registerUser():
    users = leeFichero(ficheroUsers)
    if request.is_json:
       
        user = request.get_json()
        
        password = user['password'].encode('utf-8')
      
        salt = bcrypt.gensalt()
       
        hashPassword = bcrypt.hashpw(password, salt).hex()
       
        user['password'] = hashPassword
        
        users.append(user)
       
        escribeFichero(ficheroUsers, users)
        # Devolvemos el token y 201
        token = create_access_token(identity=user['username'])
        return {'token': token}, 201
    # Si la petición no cumple con el formato JSON
    return {"error": "Request must be JSON"}, 415

@usersBP.get('/')
def loginUser():
    users = leeFichero(ficheroUsers)
    if request.is_json:
        user = request.get_json()
        # Cojo usuario y contraseña del JSON
        username = user['username']
        password = user["password"].encode('utf-8')
        # Recorro la lista de usuarios para buscar     
        for userFile in users:
            # Si coinciden el nombre de usuario del JSON con el
            # que estoy recorriendo en la lista
            if userFile['username'] == username:
                # Tomo la contraseña del usuario guardado en el fichero
                passwordFile = userFile['password']
                # Comparamos las contraseñas
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    # Generamos el token para el usuario
                    token = create_access_token(identity=username)
                    # Devolvemos el token generado
                    return {'token': token}, 200
                else:
                    # Si las contraseñas no coinciden significa que no está autorizado
                    return {'error': 'No authorized'}, 401
        return {'error': 'User not found'}, 404
    return {"error": "Request must be JSON"}, 415
    
    