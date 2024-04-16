import requests

url_user="http://localhost:5051/users"

usuario={"username": "Ana", "password": "24326224313224424666765364644e367473587a6a70554258756f75756347332e6d6d686b4f6b4379333554506f33516556326d467030485839672e"}

respuestaUsuario=requests.get(url_user, json=usuario)

codigousuario= respuestaUsuario.status_code

if codigousuario == 200:
    json = respuestaUsuario.json() #{'token' : valor_token}
    
    valor_token =json["token"]
    cabecera={'Authorization': f'Bearer{valor_token}'}
    
    url_cliente="http://localhost:5051/clientes/10"
    
    cliente= {
      "nombre_cliente": "Anitaa",
      "direccion_envio": "Av Central , Ciudad Malaga",
      "correo_electronico": "ana@example.com",
      "numero_telefono": "987-654-1210"
    }
    
    respuestaCliente=requests.put(url_cliente, json=cliente,headers=cabecera)
    
    codigoCliente=respuestaCliente.status_code
    if codigoCliente==200:
        print("Se ha modificado el cliente")
    elif codigoCliente == 201:
        print("Se ha añadido un nuevo cliente")
    else:
        print("Ha habido algún error en la petición")
    
else:
    print("Error en la autenticación de usuario")