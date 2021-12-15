# Proyecto de monitoreo dinamico para medios naturales : Raspberry pi


## Indice:

- Componentes.
  - Ultrasonido
  - Camara
  - BMP280
  - Ds18b20
  - Ms5803
  - Tipping
- Sitio web
- Instalación del software
  - Sistema Operativo
  - Instalación del programa
  - Configuración
- Referencias.


# Componentes:

En esta sección se mostrará como montar los diferentes instrumentos que se usa en esta estación de monitoreo.

## Ultrasonido

El modo en que se conecta el US-100, es en el protocolo que usa el HC-SR04, que son igual de compatibles, pero con la gran diferencia que no necesita de resistencia.


![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/us100.png)


## Camara
Es necesario recarcar que la camara, no viene con el conector marrón que se ve en la foto. Sino con uno blanco que es compatible con modelos más grandes, por lo que hay que comprar el conector a parte.

![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/camara.png)


## BMP280 y MS5803
En este caso se hizo junta las conexiones porque en el protocolo, se usan las misma entradas (sda y slc). En que es necesario intercalar cada instrumento. Por lo tanto se usa un transistor que pueda hacer de operador logico, para evitar interferencias entre los dos insturmentos.

![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/BMP280-ms5803.png)

## Ds18b20
El sensor de temperatura se usa en la tierra. Considerar las configuraciones extra ya que el protocolo lo usa como un driver.


![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/Ds18b20.png)


## Tipping
Para este sensor es necesario tenerlo siempre en funcionamiento. Para medir la precipitación de un lugar.
![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/tipping.png)

# Instalación del software

Para la instalación de este software, el lado más fácil es clonar la memoria sd del dispositivo raspberry. Por lo cual en caso de no tenerlo a mano aquí, es necesario pasar por las siguientes instalaciones. Por otro lado se puede ir a la sección de la configuración.  

## Sistema Operativo

Instalar el sistema operativo de la raspberry pi, en una memoria sd. Para más información consulte la página oficial. https://www.raspberrypi.org/
Es necesario que se conecte a al dispositivo wifi que va a acompañar el dispositivo. (El dispositivo wifi - LTE 4g/3g)

## Instalación del programa

En Documentos abra el terminal e ingrese lo siguiente:

`` sudo apt install git``

`` git clone https://github.com/SebastianDuranV/MonitoreoDinamicoInstrumentos.git ``

``pip3 install -r requirements.txt``

El gran paso en que se tendrá que preguntar en las referencias, en que tendrá que configurar el sistema operativo para que habilite ciertas entradas. Que son en el caso del sensor Ds18b20, Bmp280, por lo cual puede consultar las respectivas referencias. En la que no siempre pueda funcionar con otros dispositivos semejantes. Por lo que se le recomienda verificar las fuentes.

## Configuración

Para configurar el nodo es necesario establecer ciertos paramentros.
Uno de ellos es importante inicializar el nodo en el sitio web - cuencaustral. Por lo que en cuencaustral.cl puedes ir al modo editor en que, se registra al ingresar como administrador,veras la siguiente página.
![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/modoeditor.png)


El siguiente poso es ir a "Crear -> Nodo" ingresa los datos que son el nombre, latitud, longitud, descripción o cuerpo.

![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/modoeditor-hambur.png)

![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/crearnodo.png)

Luego te entregará una id que deberás ingresar en el archivo "config.json".

![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/resultado.png)

En la que tendrás que cambiar los numeros, de las configuraciones en que ademas de cambiar el identificador (id), puedes cambiar las frecuencias, de cada cuantos minutos se encenderá y obtendrá los datos.

``{``
``	"id": 1 ,``

``"instrumentos"  :``
``{``

``"camara": {"frecuencia": 2 },``

``"ms5803":{"frecuencia": 3 },``

``"bmp280":{"frecuencia": 2 },``

``"ds18b20":{ "frecuencia": 2 },``

``"ultrasonido": { "frecuencia" : 2 },``

``"tipping": {"frecuencia" : 2 }``

``}``
``}``

Por lo que en la pagina de cuencaustral.cl, al momento de encender la raspberry, empezará a enviar datos directamente a la los servidores por lo que se podrá visualizar los graficos, foto y video que se mostrará en el sitio.
En el sitio de web, en el inicio desde "Monitoreo -> Dinamico", busca donde colocaste el nodo o la raspberry. Entra al nodo y vas a visualizar la información que recolecta la raspberry.

![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/mapa.png)


Por otro lado tienes en el modo editor, la forma de visualizar los nodos que se ha hecho, ademas de poder eliminar y editar cada nodo. En los botones disponible en la info de cada nodo o en la lista. "Lista -> Nodo"

![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/mostrar1.png)

![alt text](https://raw.githubusercontent.com/SebastianDuranV/MonitoreoDinamicoInstrumentos/master/imagenes/mostrar2.png)

  NOTA: LA RASPBERRY DEBE ESTAR CONECTADO CORRECTAMENTE CON TODOS LOS INSTRUMENTOS, DE LO CONTRARIO NINGÚN DATO SE VISUALIZARA, POR LO QUE DEBES ASEGURARTE QUE SE ENVÍE EL PRIMER DATO, AL MOMENTO DE INSTALAR. 

# Referencias.

### Ultreasonido:
- https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/python-circuitpython

### Camara:
- https://www.youtube.com/watch?v=oo0A_yRrIxQ&t=426s&ab_channel=SPARKLERS%3AWeAreTheMakers

### Bmp280:
- https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2
  
### Ds18b20:
- https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/2
  
### Ms5803:
- https://pypi.org/project/ms5803py/
  
### Tipping:
- https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/8

## Global:
Este es otro proyecto, es necesario
- https://www.youtube.com/watch?v=0gNnUWtbmeI&t=571s&ab_channel=devaslife