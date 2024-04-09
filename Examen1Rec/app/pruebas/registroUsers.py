import requests
url="http://localhost:5050/users"

usuario={"username":"britany","password":"1234"}

respuesta=requests.post(url,json=usuario)
num=respuesta.status_code

if num==201:
    print(respuesta.json())
print (respuesta.status_code)