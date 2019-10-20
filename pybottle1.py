from bottle import Bottle, route, run, template, request, get, post
import sqlite3


@route('/')
def index():
    conn = sqlite3.connect('test1.db')
    c = conn.cursor()
    c.execute('select * from employee')
    result = c.fetchall()
    conn.close()
    return template('index', rows=result)

def register():
    new = request.GET.task.strip()

    conn = sqlite3.connect('test1.db')
    c = conn.cursor()
    c.execute('INSERT INTO employee VALUES(?,?,?,?,?), (id, name, email, section, age)')
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
'''
    conn = sqlite3.connect("test1.db")
    c = conn.cursor()
    c.execute("INSERT INTO employee VALUES(?,?,?,?,?), (id, name, email, section, age)")
    #new-employee = c.lastrowid
    conn.commit()
    c.dlose
    return template('index', rows=new-employee)
'''




run(host='localhost', port=8080, debug=True, reloader=True)
