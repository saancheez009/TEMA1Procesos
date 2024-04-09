import requests

url="http://localhost:5050/peliculas/1/actores"

respuesta=requests.get(url)
codigo=respuesta.status_code

if codigo==200:
    print("Petición correcta")
    print(respuesta.json())
else:
    print("Petición incorrecta")