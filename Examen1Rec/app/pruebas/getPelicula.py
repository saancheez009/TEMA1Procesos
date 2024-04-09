import requests

url="http://localhost:5050/peliculas/1"
respuesta = requests.get(url)
codigo=respuesta.status_code

if codigo==200:
    print("Peticioón correcta:")
    json=respuesta.json()
    print("id:",json["id"])
    print("Título:",json["titulo"])
    print("Año lanzamiento:",json["anyoLanzamiento"])
    
else:
    print("El recurso no existe")
    