import socket
import requests

host = '192.168.1.10'
port = 8080
#addr = (host, port)
addr = 'http://' + host + ':' + str(port) + "/"

auth_data = {'temperatura': '15.3', 'humendad': '14','imagen':'Aqui va una imagen','distancia':'213', 'precipitacion': '23 mm'}
try:
    resp = requests.post(addr, data=auth_data)
    print("Enviado")
except:
    print("No enviado")