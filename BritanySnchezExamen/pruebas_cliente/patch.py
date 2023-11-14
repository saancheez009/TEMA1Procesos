import requests
#url que ha dado al ejecutar el __init__ de la carpeta app
api_url=""

todo={"nombre":"ADC"}

response = requests.patch(api_url, json=todo)

print(response.json())
print(response.status_code)