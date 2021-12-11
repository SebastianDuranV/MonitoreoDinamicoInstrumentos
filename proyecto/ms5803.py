# Instrmento para medir la presión y la temperatura del agua.
from instrumento import Instrumento
import ms5803py
import time

class Ms(Instrumento):

    def obtenerDatos(self):
        
        s = ms5803py.MS5803()
    
        press, temp = s.read(pressure_osr=512)
        print("quick'n'easy pressure={} mBar, temperature={} C".format(press, temp))
        raw_temperature = s.read_raw_temperature(osr=4096)

        for i in range(5):
            raw_pressure = s.read_raw_pressure(osr=256)
            press, temp = s.convert_raw_readings(raw_pressure, raw_temperature)
            print("advanced pressure={} mBar, temperature={} C".format(press, temp))

        dato = { "presion" : press, "temperatura": temp, "data": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}

        self.guardarDatos("ms5803",dato)
        return dato    
