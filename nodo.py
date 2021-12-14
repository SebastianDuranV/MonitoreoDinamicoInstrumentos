# encoding: utf-8
# Implementación de las principales funciones del nodo
import requests
import time
from os import system
from csv import writer
import csv
import os
import glob2 as glob
import base64

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

        self.instrumentos.append(Camara(config["instrumentos"]["camara"],"camara"))
        self.instrumentos.append(Bmp(config["instrumentos"]["bmp280"],"bmp280"))
        self.instrumentos.append(Ms(config["instrumentos"]["ms5803"], "ms5803"))
        self.instrumentos.append(Ds(config["instrumentos"]["ds18b20"], "ds18b20"))
        self.instrumentos.append(Ultrasonido(config["instrumentos"]["ultrasonido"], "ultrasonido"))
        self.instrumentos.append(Tipping(config["instrumentos"]["tipping"], "tipping"))

    def loop(self):
       
        system('clear')
        
        while True:
            
            s = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

            if s[17:19] == '00': 
                for instrumento in self.instrumentos:
                    if self.count % instrumento.obtenerFrecuencia() == 0:
                        print(instrumento.obtenerFrecuencia())
                        dato = instrumento.obtenerDatos()
                        self.enviarDatosServidor(dato, instrumento.obtenerNombre())
            
                time.sleep(1)
                self.count += 1
            else:
                #system('clear')
                print(s)
                print(self.count)
                time.sleep(1)
         


    def enviarDatosServidor(self,datos, instrumento):
        # En data debe ir los datos que se van a enviar.
        if instrumento != "camara":
            self.enviarDatosGuardados(instrumento)
        else:
            self.enviarFotos()
        
        try:
            requests.post(url = self.url + '/' + str(self.id) + '/' + instrumento , json = datos)
        except:
            self.guardarEnNodoDatos(datos, instrumento)

    # Guarda en nodo los datos en caso de que no se puedan enviar los datos
    def guardarEnNodoDatos(self,datos, instrumento):
        if self.existeArchivo(instrumento + '.csv') == False:
            with open(instrumento + '.csv', 'a', newline='') as f_object:  
                writer_object = writer(f_object)
                writer_object.writerow(datos)  
                f_object.close()
                print("Nombres guardados")
        
        if instrumento != "camara":
            with open(instrumento + '.csv', 'a', newline='') as f_object:  
                writer_object = writer(f_object)
                writer_object.writerow(datos.values())  
                f_object.close()
                print("guardado")
        else:
            with open(instrumento + '.csv', 'a', newline='') as f_object:  
                writer_object = writer(f_object)
                writer_object.writerow(datos['data'])  
                f_object.close()
                print("guardado")        

            info = datos['dato']
            info = base64.b64decode(info)
            image_result = open(datos['data'] +'.jpg', 'wb')
            # create a writable image and write the decoding result
            image_result.write(info)


    # Comprueba si esta el archivo
    def existeArchivo(self,filePath):
        try:
            with open(filePath, 'r') as f:
                return True
        except FileNotFoundError as e:
            return False
        except IOError as e:
            return False


    # Si encuentra los archivos los envia y los elimina, sino, no hace nada.
    def enviarDatosGuardados(self,instrumento):
        if self.existeArchivo(instrumento + '.csv'):
            print("hay archivos guardados")

            # Abre el archivo y lo envia en forma de diccionario
            with open(instrumento + '.csv', mode='r') as inp:
                reader = list(csv.reader(inp))
                for i in range(1,len(reader)):
                    
                    print("a")
                    datos = {}

                    for j in range(len(reader[0])):
                        datos[reader[0][j]] = reader[i][j]
                    
                    print(datos[reader[0][j]])

                    try:
                        print("datos guardados enviados")
                        requests.post(url = self.url + '/' + str(self.id) + '/' + instrumento , json = datos)
                    except:
                        return 0
            
            # Eliminar archivo de los datos guardados
            print("eliminar: " + instrumento)
            os.remove(instrumento + ".csv")
            return 0

        else:
            return 0


    def enviarFotos(self):

            listaFotos = glob.glob('*.jpg')
            listaFotos.sort()
    
            for nombreFoto in listaFotos:
                with open(nombreFoto, mode='rb') as file:
                    img = file.read()
                datos = { "dato" : base64.b64encode(img), "data": nombreFoto[:len(nombreFoto)-4]}
                requests.post(url = self.url + '/' + str(self.id) + '/camara' , json = datos)
                os.remove(nombreFoto)

