import requests

url_user="http://localhost:5050/users"

usuario={"username":"britany","password":"h"}

respuestaUsuario=requests.get(url_user, json=usuario)

codigousuario= respuestaUsuario.status_code

if codigousuario == 200:
    json = respuestaUsuario.json() #{'token' : valor_token}
    
    valor_token =json["token"]
    cabecera={'Authorization': f'Bearer{valor_token}'}
    
    urlActor="http://localhost:5050/actores/1"
    respuestaActor=requests.delete(urlActor,headers=cabecera)
    
    if respuestaActor==200:
        print("Actor eliminado correctamente")
    else:
        print("No se ha podido eliminar el actor")
        
elif codigousuario==401:
    print("No se encontró el usuario")
        
else:
    print("Error en el login")
    