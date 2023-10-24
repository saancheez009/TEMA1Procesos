import requests

def mostrar():
    url="https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if (response.status_code==200):
        print("Código de estado: ",response.status_code)
        print(response.json())
    else:
        print("Ha habido un error")
    



def publicacion_concreta(publicacion):
    
    url="https://jsonplaceholder.typicode.com/posts/"+publicacion
    response = requests.get(url)

    if (response.status_code==200):
        print("Código de estado: ",response.status_code)
        print(response.json())
    else:
        print("Ha habido un error")



def añadir_publicacion(idUsuario,titulo,cuerpo):

    url="https://jsonplaceholder.typicode.com/posts"

    dict ={'userId':idUsuario, 'title':titulo, 'body':cuerpo}

    response= requests.post(url, json=dict)

    if (response.status_code==200):
        print("Código de estado: ",response.status_code)
        print(response.json())
    else:
        print("Ha habido un error")



def modificar_publicacion(publicacion,idUsuario,titulo,cuerpo):

    url="https://jsonplaceholder.typicode.com/posts/"+publicacion

    response = requests.get(url)

    diccionario={'userId':idUsuario,'title':titulo,'body':cuerpo}

    response=requests.put(url, json=diccionario)
    if (response.status_code==200):
        print("Código de estado: ",response.status_code)
        print(response.json())
    else:
        print("Ha habido un error")
        
        
def modificar_dato(publicacion,dato):

    url="https://jsonplaceholder.typicode.com/posts/"+publicacion

    response = requests.get(url)
    
    if dato=="idUsuario":
        idUsuario=input("Introduzca un id de usuario: ")
        diccionario={'userId':idUsuario}
        response=requests.put(url, json=diccionario)

        if (response.status_code==200):
            print("Código de estado: ",response.status_code)
            print(response.json())
        else:
            print("Ha habido un error")

    elif dato=="titulo":
        titulo=input("Introduca un título: ")
        diccionario={'title':titulo}
        response=requests.put(url, json=diccionario)
        if (response.status_code==200):
            print("Código de estado: ",response.status_code)
            print(response.json())
        else:
            print("Ha habido un error")

    elif dato=="cuerpo":
        cuerpo=input("Introduzca el cuerpo de la publicación: ")
        diccionario={'body':cuerpo}
        response=requests.put(url, json=diccionario)
        
        if (response.status_code==200):
            print("Código de estado: ",response.status_code)
            print(response.json())
        else:
            print("Ha habido un error")



def eliminar(publicacion):

    url="https://jsonplaceholder.typicode.com/posts/"+publicacion

    response = requests.delete(url)
    if (response.status_code==200):
        print("Código de estado: ",response.status_code)
        print(response.json())
    else:
        print("Ha habido un error")