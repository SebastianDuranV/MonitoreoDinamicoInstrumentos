from gpiozero import Button 
import time

rain_sensor = Button(6)
BUCKET_SIZE = 0.2794
count = 0

def bucket_tipped():
    global count
    count = count + 1
    #print (count * BUCKET_SIZE)

def reset_rainfall():
    global count
    count = 0



rain_sensor.when_pressed = bucket_tipped

while True:
    time.sleep(2)
    rain = count * BUCKET_SIZE
    reset_rainfall()
    print(rain)


