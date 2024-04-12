import requests
url_user="http://localhost:5051/users"

usuario={"username": "ana", "password": "24326224313224424666765364644e367473587a6a70554258756f75756347332e6d6d686b4f6b4379333554506f33516556326d467030485839672e"}

respuestaUsuario=requests.get(url_user, json=usuario)

codigousuario= respuestaUsuario.status_code


pedido= {
      "fecha_pedido": "2024-02-16",
      "total_pedido": 175.20,
      "estado_pedido": "Entregado",
      "id_cliente": 1
    }
if codigousuario == 200:
    json = respuestaUsuario.json() #{'token' : valor_token}
    
    valor_token =json["token"]
    cabecera={'Authorization': f'Bearer{valor_token}'}
    
    url="http://localhost:5051/pedidos/"
    respuesta=requests.post(url,headers=cabecera)
    
    if respuesta==200:
        print("pedido agregado correctamente")
    else:
        print("No se ha podido agregar el pedido")
        
elif codigousuario==401:
    print("No se encontró el usuario")
        
else:
    print("Error en el login")


