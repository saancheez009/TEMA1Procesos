from funciones import*

url="https://jsonplaceholder.typicode.com/posts"

num=1


while num !=0:
    print("\nSeleccione una opción")
    print("1. Mostrar todas las publicaciones")
    print("2. Mostrar una publicación concreta")
    print("3. Añadir una nueva publicación")
    print("4. Modificar todos los datos de una publicación")
    print("5. Modificar un dato concreto de una publicación")
    print("6. Eliminar una publicación")
    print("0. Salir de la aplicación")
    
    num=int(input())
    
    if num == 1:

        mostrar()

    elif num==2:

        publicacion=input("Por favor introduzca la publicación que desea mostrar")
        publicacion_concreta(publicacion)

    elif num==3:

        idUsuario=input("Introduzca un id de usuario: ")
        titulo=input("Introduca un título: ")
        cuerpo=input("Introduzca el cuerpo de la publicación: ")

        añadir_publicacion(idUsuario,titulo,cuerpo)
    elif num==4:
        publicacion=input("Por favor introduzca la publicación que desea modificar: ")

        idUsuario=input("Introduzca un id de usuario: ")
        titulo=input("Introduca un título: ")
        cuerpo=input("Introduzca el cuerpo de la publicación: ")

        modificar_publicacion(publicacion,idUsuario,titulo,cuerpo)
    elif num==5:
        publicacion=input("Por favor introduzca la publicación que desea modificar: ")
        dato=input("Por favor introduzca el dato que desea modificar: \nidUsuario\ntitulo\ncuerpo\n")
        
        modificar_dato(publicacion,dato)
    elif num==6:
        publicacion=input("Por favor introduzca la publicación que desea eliminar: ")
        eliminar(publicacion)
    

print("Usted ha salido de la aplicación")
