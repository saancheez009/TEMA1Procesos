import requests

url_user="http://localhost:5051/users"

usuario={"username": "ana", "password": "24326224313224424666765364644e367473587a6a70554258756f75756347332e6d6d686b4f6b4379333554506f33516556326d467030485839672e"}

respuestaUsuario=requests.get(url_user, json=usuario)

codigousuario= respuestaUsuario.status_code

if codigousuario == 200:
    json = respuestaUsuario.json() #{'token' : valor_token}
    
    valor_token =json["token"]
    cabecera={'Authorization': f'Bearer{valor_token}'}
    
    urlCliente="http://localhost:5051/clientes/5"
    respuestaCliente=requests.delete(urlCliente,headers=cabecera)
    
    if respuestaCliente==200:
        print("Cliente eliminado correctamente")
    else:
        print("No se ha podido eliminar el cliente")
        
elif codigousuario==401:
    print("No se encontró el usuario")
        
else:
    print("Error en el login")