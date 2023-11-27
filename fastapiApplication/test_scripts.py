# test_script.py
import requests

url = "http://127.0.0.1:8000/todos"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = {
    "name": "Buy groceries",
    "description": "Go to the supermarket and buy some essentials",
    "price": 20.0,
    "tax": 2.0,
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
