# Instrumento que mide la temperatura del suelo
from instrumento import Instrumento
import time                             #Importamos el paquete time
from w1thermsensor import W1ThermSensor #Importamos el paquete W1ThermSensor

class Ds(Instrumento):

    def obtenerDatos(self):
        sensor = W1ThermSensor() #Creamos el objeto sensor

        for i in range(5):
            temperature = sensor.get_temperature()
            #Obtenemos la temperatura en centígrados
            #print("The temperature is %s celsius" % temperature)

        dato = { "temperatura" : temperature,
                    "data": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}

        self.guardarDatos("ds18b20",dato)
        return dato 

