import requests
url="http://localhost:5050/"
actor= {
        
        "nombre": "Gwyneth Paltrow",
        "nacionalidad": "estadounidense",
        "idPelicula": 2
    }

respuesta=requests.post(url,json=actor)
codigo=respuesta.status_code

if codigo==201:
    print("ACTOR añadido")
    
elif codigo == 404:
    print("La pelicula no existe")
elif codigo ==415:
    print("El JSON no es correcto")
else:
    print("Petición incorrecta")