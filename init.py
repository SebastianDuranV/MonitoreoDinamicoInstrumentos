# encoding: utf-8

from nodo import Nodo
import json


url = "http://192.168.1.11:4000/api/post" 

with open("config.json", "r") as configJson:
    config = json.load(configJson)

    #iniciando nodo
    nodo = Nodo(url, config)
   
    # Iniciar el loop para obtener los datos
    nodo.loop() 
