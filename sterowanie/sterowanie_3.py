from flask import Flask
import json

app = Flask(__name__)


@app.route('/set_params/<interval>/<mqtt>/<http>/<state>', methods=['GET'])
def set_params(interval, mqtt, http, state):
    p = dict()
    p['interval'] = interval
    p['mqtt'] = mqtt
    p['http'] = http
    p['state'] = state
    content = json.dumps(p)

    with open('../files/params_3.json', 'w') as file:
        file.write(content)

    return p


@app.route('/get_status', methods=['GET'])
def get_status():
    with open("C:/PyCharm/InternetRzeczy/smart_home/files/params_3.json", 'r') as file:
        content = file.read()
        print(content)
        return content


if __name__ == '__main__':
    app.run(port=6003, debug=True)
