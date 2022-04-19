import sqlite3

con = sqlite3.connect('zadanie6.db')
cur = con.cursor()
# cur.execute("select * from smarthome")
cur.execute("delete from smarthome")
t = cur.fetchall()
print(t)
con.commit()
con.close()
