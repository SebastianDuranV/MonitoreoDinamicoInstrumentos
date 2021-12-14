# Medir la presion, humedad y temperatura del aire.
from instrumento import Instrumento
import smbus2
import bme280
import time
import RPi.GPIO as gpio


class Bmp(Instrumento):
    
    def obtenerDatos(self):

        port = 1
        address = 0x76

        # Aciva la energía del componente
        # gpio.setmode(gpio.BOARD)
        gpio.setup(17, gpio.OUT)
        gpio.output(17, True)

        # Inicializa el instrumento
        bus = smbus2.SMBus(port)
        calibration_params = bme280.load_calibration_params(bus, address)
        
        for i in range(5):
            data = bme280.sample(bus, address, calibration_params)
 
        
        dato = { "temperatura" : data.temperature,
                "presion": data.pressure,
                "humedad": data.humidity,
                "data": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())               
                }

        self.guardarDatos("bmp280", dato)

        # Desaciva la la energía del componente
        gpio.output(17, False)

        return dato        

