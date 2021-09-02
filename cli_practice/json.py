import json
import requests

URL = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(URL)
todos = json.loads(response.text)

print(todos[0])