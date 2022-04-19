from flask import Flask, request
import json
import sqlite3

app = Flask(__name__)


@app.route('/set_params/<interval>/<mqtt>/<http>/<state>', methods=['GET'])
def set_params(interval, mqtt, http, state):
    p = dict()
    p['interval'] = interval
    p['mqtt'] = mqtt
    p['http'] = http
    p['state'] = state
    content = json.dumps(p)

    with open('C:/PyCharm/InternetRzeczy/smart_home/files/params_1.json', 'w') as file:
        file.write(content)
    return p


@app.route('/save', methods=['POST'])
def save():
    data = request.get_data(as_text=True)

    with open('C:/PyCharm/InternetRzeczy/zadanie_6/data_files/living_room', 'a') as file:
        file.write(data)
        file.write('\n')
    return data


@app.route("/read", methods=['GET'])
def read_data():
    with open('C:/PyCharm/InternetRzeczy/zadanie_6/data_files/living_room', 'r') as file:
        content = file.read()
        return content


@app.route('/get_status', methods=['GET'])
def get_status():
    with open("C:/PyCharm/InternetRzeczy/zadanie_6/files/params_1.json", 'r') as file:
        content = file.read()
        print(content)
        return content


if __name__ == '__main__':
    app.run(port=6001, debug=True)
