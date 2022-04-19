import json
import random

import requests
import paho.mqtt.client as mqtt
import numpy as np
from time import sleep


temp = random.randint(960, 1020)
while True:
    with open("C:/PyCharm/InternetRzeczy/smart_home/files/params_3.json", 'r') as file:
        params = json.load(file)

    if params['state'] == 'on':
        change = np.random.uniform(-0.5, 0.5)
        temp += change
        temp = round(temp, 1)
        message = 'livingroom' + '#' + str(temp) + '#' + 'air pressure'

        if params['http'] == 'yes':
            requests.post('http://127.0.0.1:6004/get_data', message)
        if params['mqtt'] == 'yes':
            client = mqtt.Client('garden')
            client.connect('broker.emqx.io')
            client.publish('smarthouse', message)
        print(temp)
    sleep(int(params['interval']))
