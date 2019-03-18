import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
buttonPin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

i = 0
light = "off"

while True:  
  if (GPIO.input(buttonPin)):
    if light == "on":
      #print "Light already on, waiting 1s"
      time.sleep(1)
    i += 1
    #print "TRUE, ADDING ONE"
    if i > 1:
      if light != "on":
        #print "i > 1, TURNING ON"
        os.system("python /stuff/06-vanlights/allwhite.py --candle")
        light = "on"
    time.sleep(1)
  else:
    #print "FALSE, setting to zero and light off"
    os.system("python /stuff/06-vanlights/allwhite.py --off")
    light = "off"
    i = 0
