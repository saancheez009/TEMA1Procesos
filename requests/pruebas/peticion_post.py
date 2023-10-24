import requests

url="https://jsonplaceholder.typicode.com/posts"

dict ={'userId':2, 'title':"hacer tareas", 'completed':False}

response= requests.post(url, json=dict)

print("Código de estado: ",response.status_code)

print(response.json())