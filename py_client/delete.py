from sys import argv
import requests

id = int(argv[1])

url = f"http://localhost:5173/api/productos/{ id }/"


response = requests.delete(url)

print(response)
    