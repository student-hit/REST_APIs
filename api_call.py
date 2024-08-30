import requests

response = requests.get("http://127.0.0.1:8000/api/products?format=json")

data = response.json()
print(data)