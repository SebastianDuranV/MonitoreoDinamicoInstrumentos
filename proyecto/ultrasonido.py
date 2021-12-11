# Instrumento que mide la distancia (o la altura del rio)
from instrumento import Instrumento
import time
import board
import adafruit_hcsr04


class Ultrasonido(Instrumento):

    def __init__(self,config):
        self.sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D26)
        super().__init__(config)
    
    def obtenerDatos(self):
       
        while True:
            try:
                dato = {"distancia" : self.sonar.distance,
                        "data": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}

                self.guardarDatos("camara",dato)
                return dato

            except RuntimeError:
                print("Retrying!")
