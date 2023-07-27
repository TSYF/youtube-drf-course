import requests

url = "http://localhost:5173/api/"

response = requests.post(url, json={"title": "Hello World!"})
# , params={"abc": 123}, json={"query": "Hello World!"}
# print(response)
print(response.json())
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(response)
    