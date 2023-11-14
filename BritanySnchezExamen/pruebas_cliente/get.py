import requests
#url que ha dado al ejecutar el __init__ de la carpeta app
api_url=""

response = requests.get(api_url)
print(response.json())