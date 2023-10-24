"""Escribe un programa que tome una cadena de texto como entrada y genere un diccionario que cuente la frecuencia de cada palabra en el texto."""

# Función para contar la frecuencia de palabras en un texto
def contar_frecuencia(texto):
    # Dividir el texto en palabras
    palabras = texto.split()
    
    # Inicializar un diccionario para almacenar la frecuencia de las palabras
    frecuencia = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        # Eliminar signos de puntuación si es necesario
        palabra = palabra.strip('.,!?()[]{}":;')
        # Convertir la palabra a minúsculas para evitar contar palabras en mayúsculas y minúsculas como diferentes
        palabra = palabra.lower()
        # Contar la palabra y almacenar su frecuencia en el diccionario
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    
    return frecuencia

# Obtener la entrada del usuario
texto = input("Introduce una cadena de texto: ")

# Obtener el diccionario de frecuencia de palabras
diccionario_frecuencia = contar_frecuencia(texto)

# Mostrar el diccionario de frecuencia de palabras
print("Frecuencia de palabras:")
for palabra, frecuencia in diccionario_frecuencia.items():
    print(f"{palabra}: {frecuencia}")


