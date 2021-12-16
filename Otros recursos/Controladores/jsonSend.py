import requests
r = requests.post('http://192.168.1.10:8000/', json={"key": "value"})
print("enviado")

