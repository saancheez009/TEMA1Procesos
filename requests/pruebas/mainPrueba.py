import requests

"""
#Mostrar todas las publicaciones

url="https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if (response.status_code==200):
    print("Código de estado: ",response.status_code)
    print(response.json())
else:
    print("Ha habido un error")
"""

#---------------------------------------------------------

"""
Mostrar una publicación específica

publicacion=input("Introduzca ")
url="https://jsonplaceholder.typicode.com/posts/"+publicacion
response = requests.get(url)

print("Código de estado: ",response.status_code)
print(response.json())
    """
#---------------------------------------------------------
"""Añadir una publicación

idUsuario=input("Introduzca un id de usuario: ")
titulo=input("Introduca un título: ")
cuerpo=input("Introduzca el cuerpo de la publicación: ")

url="https://jsonplaceholder.typicode.com/posts"

dict ={'userId':idUsuario, 'title':titulo, 'body':cuerpo}

response= requests.post(url, json=dict)

print("Código de estado: ",response.status_code)

print(response.json())
"""
#--------------------------------------------------

"""Modificar publicación

publicacion=input("Por favor introduzca la publicación que desea modificar: ")
idUsuario=input("Introduzca un id de usuario: ")
titulo=input("Introduca un título: ")
cuerpo=input("Introduzca el cuerpo de la publicación: ")

url="https://jsonplaceholder.typicode.com/posts/"+publicacion

response = requests.get(url)


diccionario={'userId':idUsuario,'title':titulo,'body':cuerpo}

response=requests.put(url, json=diccionario)

print("Código de estado: ",response.status_code)

print(response.json())

"""
#----------------------------------------------------------------
"""Modificar dato concreto
publicacion=input("Por favor introduzca la publicación que desea modificar: ")
dato=input("Por favor introduzca el dato que desea modificar: \nidUsuario\ntitulo\ncuerpo\n")


url="https://jsonplaceholder.typicode.com/posts/"+publicacion

response = requests.get(url)

if dato=="idUsuario":
    idUsuario=input("Introduzca un id de usuario: ")
    diccionario={'userId':idUsuario}
    response=requests.put(url, json=diccionario)
    print("Código de estado: ",response.status_code)

    print(response.json())

elif dato=="titulo":
    titulo=input("Introduca un título: ")
    diccionario={'title':titulo}
    response=requests.put(url, json=diccionario)
    print("Código de estado: ",response.status_code)

    print(response.json())

elif dato=="cuerpo":
    cuerpo=input("Introduzca el cuerpo de la publicación: ")
    diccionario={'body':cuerpo}
    response=requests.put(url, json=diccionario)
        
    print("Código de estado: ",response.status_code)

    print(response.json()) """

#--------------------------------------------------

