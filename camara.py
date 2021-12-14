# encoding: utf-8
# Implementación de la camara de la raspberry.
from picamera import PiCamera
import time
from instrumento import Instrumento
import base64


class Camara(Instrumento):

    def __init__(self,config, nombre):
        self.camara = PiCamera()
        super().__init__(config, nombre)
    
    
    def obtenerDatos(self):
        self.camara.resolution = (640, 480)
        self.camara.vflip = True

        self.camara.start_preview()
        time.sleep(2)
        self.camara.capture("test.jpg")

        with open('test.jpg', mode='rb') as file:
            img = file.read()

        dato = { "dato" : base64.b64encode(img), "data": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}

        self.guardarDatos("camara",dato)
        return dato 
