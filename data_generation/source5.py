import json
import random

import requests
import paho.mqtt.client as mqtt
import numpy as np
from time import sleep


# Humidity generator
temp = random.randint(20, 90)
while True:
    with open("C:/PyCharm/InternetRzeczy/smart_home/files/params_3.json", 'r') as file:
        params = json.load(file)

    if params['state'] == 'on':
        change = np.random.uniform(-1, 1)
        temp += change
        temp = round(temp, 1)
        message = 'livingroom' + '#' + str(temp) + '#' + 'humidity'

        if params['http'] == 'yes':
            requests.post('http://127.0.0.1:6005/get_data', message)
        if params['mqtt'] == 'yes':
            client = mqtt.Client('garden')
            client.connect('broker.emqx.io')
            client.publish('smarthouse', message)
        print(temp)
    sleep(int(params['interval']))
