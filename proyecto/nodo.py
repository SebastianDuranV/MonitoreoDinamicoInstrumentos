# encoding: utf-8
# Implementación de las principales funciones del nodo
import requests
import time
from os import system

class Nodo:

    def __init__(self, url , config):
        self.id = config["id"]
        self.url = url
        self.tiempoInicio = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.count = 0
        self.instrumentos = []

        #Insrumentos de medición
        from camara import Camara
        from bmp280s import Bmp 
        from ms5803 import Ms
        from ds18b20 import Ds
        from ultrasonido import Ultrasonido
        from tipping import Tipping

        self.instrumentos.append(Camara(config["instrumentos"]["camara"]))
        self.instrumentos.append(Bmp(config["instrumentos"]["bmp280"]))
        self.instrumentos.append(Ms(config["instrumentos"]["ms5803"]))
        self.instrumentos.append(Ds(config["instrumentos"]["ds18b20"]))
        self.instrumentos.append(Ultrasonido(config["instrumentos"]["ultrasonido"]))
        self.instrumentos.append(Tipping(config["instrumentos"]["tipping"]))

    def loop(self):
       
        system('clear')
        
        while True:
            
            s = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

            if s[17:19] == '00': 
                for instrumento in self.instrumentos:
                    if self.count % instrumento.obtenerFrecuencia() == 0:
                        print(instrumento.obtenerFrecuencia())
                        dato = instrumento.obtenerDatos()
                        self.enviarDatosServidor(dato)
            
                time.sleep(1)
                self.count += 1
            else:
                system('clear')
                print(s)
                print(self.count)
                time.sleep(1)
         


    def enviarDatosServidor(self,data):
        # En data debe ir los datos que se van a enviar.
        requests.post(url = self.url , json = data)


