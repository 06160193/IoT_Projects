#!/usr/bin/python3
import RPi.GPIO as GPIO


import requests
import numpy as np
import time
import json
import configparser
 
v=34300
TRIGGER_PIN=16
ECHO_PIN=18

def measure() :
   GPIO.output(TRIGGER_PIN, GPIO.HIGH)
   time.sleep(0.00001)  #10us
   GPIO.output(TRIGGER_PIN, GPIO.LOW)

   while GPIO.input(ECHO_PIN) == GPIO.LOW :
        pulse_start=time.time()
        
   while GPIO.input(ECHO_PIN) == GPIO.HIGH :
        pulse_end=time.time()
        
   t=pulse_end-pulse_start
   d=t*v/2
   
   return d

GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

config = configparser.ConfigParser()
config.read('../../cht.conf')
projectKey = config.get('device-key', 'projectKey')
deviceId   = config.get('device-key', 'deviceId')
sensorId   = config.get('device-key', 'sensorId')

apiURL = 'http://iot.cht.com.tw/iot/v1/device/' + deviceId + '/rawdata'
headers = { 
    "CK":projectKey,
    "Content-Type": "application/json",
}   


#t = str(time.strftime("%Y-%m-%dT%H:%M:%S"))

for x in range(30):
    value=round(measure(),2)
    #payload=[{"id":"hcsr04","value":[value]}]
    payload=[{"id":"hcsr04","value":[value]}]
    #print(payload)
    response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
    #print(response.text)
    print(value)

