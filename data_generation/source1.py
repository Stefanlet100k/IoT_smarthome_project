import json
import random

import requests
import paho.mqtt.client as mqtt
import numpy as np
from time import sleep


temp = random.randint(19, 22)
while True:
    with open("C:/PyCharm/InternetRzeczy/smart_home/files/params_1.json", 'r') as file:
        params = json.load(file)

    if params['state'] == 'on':
        change = np.random.uniform(-0.3, 0.3)
        temp += change
        temp = round(temp, 1)
        message = 'livingroom' + '#' + str(temp) + '#' + 'temperature'

        if params['http'] == 'yes':
            requests.post('http://127.0.0.1:6001/save', str(message.split('#')))
        if params['mqtt'] == 'yes':
            client = mqtt.Client('living_room')
            client.connect('broker.emqx.io')
            client.publish('smarthouse', message)
        print(temp)
    sleep(int(params['interval']))
