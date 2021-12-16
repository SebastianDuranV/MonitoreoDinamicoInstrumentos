# Mide la presipitacion del ambiente
from instrumento import Instrumento
from gpiozero import Button 
import time


class Tipping(Instrumento):

    def bucket_tipped(self):
#        global count
        self.count = self.count + 1
        print (self.count * 0.2794)

    def reset_rainfall(self):
#        global count
        self.count = 0


    def obtenerDatos(self):
        rain_sensor = Button(6)
        BUCKET_SIZE = 0.2794
        self.count = 0

        rain_sensor.when_pressed = self.bucket_tipped

        while True:
            time.sleep(10)
            rain = self.count * BUCKET_SIZE
            self.reset_rainfall()
            
            dato = { "precipitacion" : rain, "data": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}

            self.guardarDatos("tipping",dato)
            return dato



