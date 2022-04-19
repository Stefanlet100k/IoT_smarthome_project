import json
import paho.mqtt.client as mqtt
import sqlite3
import datetime


conn = sqlite3.connect('zadanie6.db')


def on_message(client, userdata, message):
    # requests.post('http://127.0.0.1:8083/upload', json=message.payload.decode('utf-8'))
    data = message.payload.decode('utf-8')
    t = data.split('#')
    name = t[0]
    value = t[1]
    print(name)
    print(value)
    cur = conn.cursor()
    cur.execute('INSERT INTO smarthome (timestamp, room, temperature)\
                VALUES( ?, ?, ?);', (datetime.datetime.now(), name, float(value)))
    conn.commit()


mqttBroker = 'broker.emqx.io'
client = mqtt.Client('client_2')
client.connect(mqttBroker)

client.subscribe('smarthouse')
client.on_message = on_message
client.loop_forever()

conn.close()
