import requests

url_user="http://localhost:5050/users"

usuario={"username":"brit","password":"24326224313224733662646f6331346139775538586f6e3345474d4e4f467a62526b4677524e4d36796a6868614a326634434e724456726a75454375"}

respuestaUsuario=requests.get(url_user, json=usuario)

codigousuario= respuestaUsuario.status_code

if codigousuario == 200:
    json = respuestaUsuario.json() #{'token' : valor_token}
    
    valor_token =json["token"]
    cabecera={'Authorization': f'Bearer{valor_token}'}
    
    urlActor="http://localhost:5050/actores/5"
    respuestaActor=requests.delete(urlActor,headers=cabecera)
    
    if respuestaActor==200:
        print("Actor eliminado correctamente")
    else:
        print("No se ha podido eliminar el actor")
        
elif codigousuario==401:
    print("No se encontró el usuario")
        
else:
    print("Error en el login")
    