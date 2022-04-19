import sqlite3
import base64
from io import BytesIO
from flask import Flask, render_template
from matplotlib.figure import Figure

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('menu.html')


@app.route('/plot')
def plot():
    conn = sqlite3.connect('../zadanie_6/zadanie6.db')
    cur = conn.cursor()
    cur.execute("select temperature from smarthome where room like 'livingroom'")
    data_lr = cur.fetchall()
    cur.execute("select temperature from smarthome where room like 'bedroom'")
    data_br = cur.fetchall()
    cur.execute("select temperature from smarthome where room like 'garden'")
    data_garden = cur.fetchall()
    conn.commit()

    fig = Figure(facecolor='khaki')
    ax = fig.subplots()
    ax.plot(data_lr, color='c', label='livingroom')
    ax.plot(data_br, color='m', label='bedroom')
    ax.plot(data_garden, color='y', label='garden')
    ax.set_facecolor('whitesmoke')
    fig.legend()
    fig.suptitle('Temperature in SMARThome')
    fig.add_axes(label='Temp')

    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


@app.route('/plot/<room>')
def choose_plot(room):
    conn = sqlite3.connect('../zadanie_6/zadanie6.db')
    cur = conn.cursor()
    cur.execute("select temperature from smarthome where room like ?", (room,))
    data = cur.fetchall()
    conn.commit()

    fig = Figure(facecolor='khaki')
    ax = fig.subplots()
    ax.plot(data, color='orange', label=room)
    ax.set_facecolor('whitesmoke')
    fig.legend()
    fig.suptitle(f'Temperature in {room}')
    fig.add_axes(label='Temp')

    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"


if __name__ == '__main__':
    app.run(port=6886, debug=True)
