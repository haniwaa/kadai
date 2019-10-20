from bottle import route, run, template, request
import sqlite3
from testmail import mysendmail

@route('/')
def name():
    return template('index', name='kumi')


@route('/form', method=['GET', 'POST'])
def register():
    email = request.forms.email
    age = request.forms.age
    conn = sqlite3.connect('kadai.sqlite3')
    c = conn.cursor()
    new_id = c.execute('select max(id) + 1 from customerinfo').fetchone()[0]
    c.execute('insert into customerinfo values(?, ?, ?)', (new_id, email, age))

    #複数の時の例
    '''
    customer_data = [('cs03@mail.com', '20'),
                    ('cs04@mail.com', '30')]
    c.executemany("insert into customerinfo values (?,?)", customer_data)
    '''

    conn.commit()
    conn.close()
    mysendmail()
    return template('form')


@route('/mailsent')
def sendmail():
    return template('mailsent')


@route('/registered')
def register():
    conn = sqlite3.connect('kadai.sqlite3')
    c = conn.cursor()
    c.execute('select * from customerinfo')
    customer_list = []
    for row in c.fetchall():
        customer_list.append({
            "id":row[0],
            "email":row[1],
            "age":row[2]
        })

    conn.commit()
    conn.close()
    return template('registered', customer_list=customer_list)

run(host='localhost', port=8080, debug=True, reloader=True)
