# Medir la presion, humedad y temperatura del aire.
from instrumento import Instrumento
import smbus2
import bme280
import time
import RPi.GPIO as gpio
import ms5803py




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

        # Desaciva la la energía del componente
        gpio.output(17, False)


        #seccion para mostrar la presión neta del agua
        s = ms5803py.MS5803()
    
        press, temp = s.read(pressure_osr=512)
        print("quick'n'easy pressure={} mBar, temperature={} C".format(press, temp))
        raw_temperature = s.read_raw_temperature(osr=4096)

        raw_pressure = s.read_raw_pressure(osr=256)
        press, temp = s.convert_raw_readings(raw_pressure, raw_temperature)
        print("advanced pressure={} mBar, temperature={} C".format(press, temp))

        datoms = { "presion" : press, "temperatura": temp, "data": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}

        
        #resta para sacar la presion total del agua
        x = datoms["presion"] - dato["presion"]
        x = x * 1.0197 # Transforma a centimetros de agua



        dato["presionNeta"] = x

        self.guardarDatos("bmp280", dato)
        return dato        

