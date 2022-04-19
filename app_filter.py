import paho.mqtt.client as mqtt
import json


def on_message(client, userdata, message):
    data = message.payload.decode('utf-8')
    t = data.split('#')
    room = t[0]
    value = t[1]
    field = t[2]
    with open('params.json', 'r') as file:
        parameters = json.load(file)

    message = []
    if parameters['room'] == 'all' or parameters['room'] == room:
        message.append(room)
    if parameters['field'] == 'all' or parameters['field'] == field:
        message.append(value)
        message.append(field)
    if len(message) == 3:
        print(message)
        # requests.post('http://127.0.0.1:8083/upload', json=message.payload.decode('utf-8'))
        publisher = mqtt.Client('Filter')
        publisher.connect('broker.emqx.io')
        publisher.publish('sh_filtered', str(message))


mqttBroker = 'broker.emqx.io'
client = mqtt.Client('client_2')
client.connect(mqttBroker)

client.subscribe('smarthouse')
client.on_message = on_message
client.loop_forever()

