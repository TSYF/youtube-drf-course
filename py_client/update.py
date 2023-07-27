import requests
from sys import argv

id = int(argv[1])

url = f"http://localhost:5173/api/productos/{ id }/"

data = {
    "title": "This has been updated",
    "price": 69.42
}

response = requests.patch(url, json=data)

print(response.json())
    