import requests
#url que ha dado al ejecutar el __init__ de la carpeta app
api_url=""

response = requests.delete(api_url)
print(response.satatus_code)
print(response.json())