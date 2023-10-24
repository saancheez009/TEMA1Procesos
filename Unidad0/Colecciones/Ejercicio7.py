"""Crea un programa que permita al usuario agregar, eliminar y buscar contactos en una libreta de direcciones implementada como un diccionario. 
La clave del diccionario será el nombre del contacto y el valor, su número de teléfono. Crea un menú para las distintas opciones e implementa una función para cada opción."""

# Inicializar un diccionario para la libreta de direcciones
#contactos
libreta_de_direcciones = {}

# Función para agregar un contacto
def agregar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    telefono = input("Introduce el número de teléfono: ")
    libreta_de_direcciones[nombre] = telefono
    print(f"Contacto {nombre} añadido.")

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = input("Introduce el nombre del contacto que deseas eliminar: ")
    if nombre in libreta_de_direcciones:
        libreta_de_direcciones.remove(nombre)
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"El contacto {nombre} no existe en la libreta de direcciones.")

# Función para buscar un contacto
def buscar_contacto():
    nombre = input("Introduce el nombre del contacto que deseas buscar: ")
    if nombre in libreta_de_direcciones:
        telefono = libreta_de_direcciones[nombre]
        print(f"Nombre: {nombre}, Teléfono: {telefono}")
    else:
        print(f"El contacto {nombre} no existe en la libreta de direcciones.")

# Menú principal
while True:
    print("\nMenú de Libreta de Direcciones:")
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1/2/3/4): ")
    
    if opcion == '1':
        agregar_contacto()
    elif opcion == '2':
        eliminar_contacto()
    elif opcion == '3':
        buscar_contacto()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")