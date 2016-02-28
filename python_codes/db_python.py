import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table(): #set
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keywork TEXT, value REAL)')

def data_entry():#get
    c.execute("INSERT INTO stuffToPlot VALUES(1455656, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()

#f = open("document.doc", "w")
