#!/usr/bin/python3

import requests
import numpy as np
import time
import json
import configparser 
import Adafruit_DHT

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



while True:
    humidity, temperature = Adafruit_DHT.read_retry(22, 4)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        time.sleep(1)
    else:
        print('Failed to get reading. Try again!')
    t = str(time.strftime("%Y-%m-%dT%H:%M:%S"))
    
    payload=[{"id":"Temp", "value":[round(temperature,1)]},{"id":"Hum", "value":[round(humidity,1)]}]


    response = requests.post(apiURL, headers=headers, data=json.dumps(payload))
    print(response.text)
