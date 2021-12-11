# Clase padré que tendra los prinipales atributos y metodos que tendrán cada componente
import json


class Instrumento:

    def __init__(self,config):
        self.frecuencia = config["frecuencia"]
        print(config)


    def guardarDatos(self,instrumento,dato):
        try:
            with open( instrumento + '.json', 'w') as fp:
                json.dump(dato, fp)
        except:
            print("No se guardo")

    def obtenerFrecuencia(self):
        return self.frecuencia

