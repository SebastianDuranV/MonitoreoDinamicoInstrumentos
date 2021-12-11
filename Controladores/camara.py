from picamera import PiCamera
import time
import cv2

camara = PiCamera()
camara.resolution = (640, 480)
camara.vflip = True

camara.start_preview()
time.sleep(2)
camara.capture("test.jpg")

import json
import base64

data = {}
with open('test.jpg', mode='rb') as file:
    img = file.read()


data['img'] = base64.b64encode(img)
#data['img'] = base64.encodestring(img)
#print(json.dumps(data))

import requests
r = requests.post('http://192.168.1.10:8000/', json = data)
print("enviado")
