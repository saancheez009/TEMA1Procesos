import requests

url="http://localhost:5051/clientes/1/pedidos/101"

respuesta=requests.get(url)
codigo=respuesta.status_code
if codigo==200:
    print(respuesta.json())
else:
    print("El recurso no existe")