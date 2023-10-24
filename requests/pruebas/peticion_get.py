import requests

url="https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print("Código de estado: ",response.status_code)
print(response.json())

"""recorrer diccionario"""

dict= response.json()

for clave in dict:
    print(clave, ":", dict[clave])