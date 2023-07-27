import requests

url = "http://localhost:5173/api/productos/"

data = {
    "title": "Product created with Mixin",
    "price": 243.99
}

response = requests.post(url, json=data)

print(response.json())
    