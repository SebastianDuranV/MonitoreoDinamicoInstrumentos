# encoding: utf-8

from nodoTipping import Nodo
import json


url = "http://www.cuencaustral.cl/api/post" 

with open("config.json", "r") as configJson:
    config = json.load(configJson)

    #iniciando nodo
    nodo = Nodo(url, config)
   
    # Iniciar el loop para obtener los datos
    nodo.loop() 

