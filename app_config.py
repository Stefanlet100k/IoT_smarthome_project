from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('menu.html')
    else:
        d = dict()
        d['room'] = request.form['room']
        d['field'] = request.form['field']
        data = json.dumps(d)
        with open('params.json', 'w') as file:
            file.write(data)
        return render_template('second_menu.html')


if __name__ == "__main__":
    app.run(port=6006, debug=True)
