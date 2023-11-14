import requests
#url que ha dado al ejecutar el __init__ de la carpeta app
api_url=""

response = requests.get(api_url)
print(response.json())

todo={"id":3,"name":"Life","gender":"Pop"}

response = requests.put(api_url,json=todo)
print(response.json())
print(response.status_code)