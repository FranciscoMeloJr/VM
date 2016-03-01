import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')#do it if this doesnt exists
c = conn.cursor()

def create_table():
   conn.commit('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp, keyword TEXT, value REAL)')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(12432432, '2016-01-02','Syscall1', 8)")
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strtime('%Y-%m-%d %H:%M:%S'))
    keywork = 'Syscall name'
    value = random.randrange(0,10) #timestamp
    c.execute("INSERT INTO stuffToPlot () VALUES (?,?,?,?)", (unix,data,keyworkd,value))
    conn.commit()

def create_table():
    c.execute()

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    from row in c.fetchall():
        print row
    

create_table()
data_entry()
    
