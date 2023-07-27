import requests
from getpass import getpass

payload = {
    "username": input("Username: "),
    "password": getpass()
}

auth_endpoint = "http://localhost:5173/api/auth/"

auth_response = requests.post(auth_endpoint, json=payload)

if auth_response.status_code == 200:
    token = auth_response.json()["token"]
    headers = {
        "Authorization": f"Bearer { token }"
    }
    endpoint = "http://localhost:5173/api/productos/"

    response = requests.get(endpoint, headers=headers)

    print(response.json())
    

    