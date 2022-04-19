import paho.mqtt.client as mqtt
import json


def on_message(client, userdata, message):
    data = message.payload.decode('utf-8')
    print(data)


mqttBroker = 'broker.emqx.io'
client = mqtt.Client('client_just_checking')
client.connect(mqttBroker)

client.subscribe('sh_filtered')
client.on_message = on_message
client.loop_forever()

