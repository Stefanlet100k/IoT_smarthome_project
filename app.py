from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/get_avg/<room>/<period>', methods=['GET'])
def get_avg(room, period):
    con = sqlite3.connect('zadanie6.db')
    cur = con.cursor()
    if room == 'all':
        cur.execute("select avg(temperature) from smarthome where timestamp>=datetime('now', ?)", ('-'+str(period)+' minutes',))
        t = cur.fetchall()
        con.commit()
        print(t)
        return 'Average temperature in all rooms: ' + str(round(t[0][0], 2)) + ' Celcius'
    elif room == 'livingroom' or room == 'garden' or room == 'bedrooms':
        cur.execute("select avg(temperature) from smarthome where timestamp>=datetime('now', ?) and room=?",\
                    ('-'+str(period)+' minutes', room))
        t = cur.fetchall()
        con.commit()
        print(t)
        return f'Average temperature in {room}: ' + str(round(t[0][0], 2)) + ' Celcius'
    else:
        return '<h2>Error</h2>'


@app.route('/get_data', methods=['POST', 'GET'])
def get_data():
    temperature = request.json()
    print(temperature)
    print(type(temperature))
    return temperature


if __name__ == '__main__':
    app.run(port=6060, debug=True)

