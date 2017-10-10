import sqlite3
import datetime

conn = sqlite3.connect('animetheme.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS comments (id text, date date)')

def save_comment_id(comment_id):
    c.execute('INSERT INTO comments VALUES(?, ?)', (comment_id, datetime.date.today()))
    conn.commit()
    c.close()
#create_table()
