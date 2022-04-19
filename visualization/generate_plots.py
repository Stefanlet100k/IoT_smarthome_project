import matplotlib.pyplot as plt
import sqlite3
import datetime


def agregator():
    conn = sqlite3.connect('../zadanie_6/zadanie6.db')
    cur = conn.cursor()
    cur.execute("select temperature from smarthome where room like 'livingroom'")
    data_lr = cur.fetchall()
    cur.execute("select temperature from smarthome where room like 'bedroom'")
    data_br = cur.fetchall()
    cur.execute("select temperature from smarthome where room like 'garden'")
    data_garden = cur.fetchall()
    conn.commit()

    plt.plot(data_lr, color='brown', label='livingroom')
    plt.plot(data_br, color='blue', label='bedroom')
    plt.plot(data_garden, color='green', label='garden')
    plt.ylabel('temperature [C]')
    plt.title(f'Temperature in smarthome {datetime.datetime.now()}')
    plt.legend()
    plt.savefig('temperature.png')
    return 'Image saved...'
