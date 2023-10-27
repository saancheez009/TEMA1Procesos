import requests

url="http://localhost:5050/countries"

dict ={"id":6, "name": "Brasil", "capital":"Brasilia", "Area":45879}


response= requests.post(url, json=dict)

print("Código de estado: ",response.status_code)

print(response.json())