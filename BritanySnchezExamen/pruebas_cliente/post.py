import requests
#url que ha dado al ejecutar el __init__ de la carpeta app
api_url=""

#banda
todo={"id":8, "name":"Green","gender":"Pop"}

#cancion

#todo{"id":10,"titulo":"colors","Duracion":"3:20","idBanda":2}

response= requests.post(api_url, json=todo)

print(response.json())
      
print("Código de estado:", response.status_code)