import requests

url_user="http://localhost:5050/users"

usuario={"username":"brit","password":"24326224313224733662646f6331346139775538586f6e3345474d4e4f467a62526b4677524e4d36796a6868614a326634434e724456726a75454375"}

respuestaUsuario=requests.get(url_user, json=usuario)

codigousuario= respuestaUsuario.status_code

if codigousuario == 200:
    json = respuestaUsuario.json() #{'token' : valor_token}
    
    valor_token =json["token"]
    cabecera={'Authorization': f'Bearer{valor_token}'}
    
    url_pelicula="http://localhost:5050/peliculas/1"
    
    pelicula={"titulo":"Spiderman", "anyoLanzamiento":2002}
    
    respuestaPelicula=requests.put(url_pelicula, json=pelicula,headers=cabecera)
    
    codigoPelicula=respuestaPelicula.status_code
    if codigoPelicula==200:
        print("Se ha modificado la pelicula")
    elif codigoPelicula == 201:
        print("Se ha añadido una nueva pelicula")
    else:
        print("Ha habido algún error en la petición")
    
else:
    print("Error en la autenticación de usuario")