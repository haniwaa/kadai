import numpy as np
import matplotlib.pyplot as plt
import sqlite3


def get_agelist():
    conn = sqlite3.connect('kadai.sqlite3')
    c = conn.cursor()
    c.execute('select * from customerinfo')
    customer_list = []
    for row in c.fetchall():
        customer_list.append(
            row[2]
        )
    x = customer_list

    conn.commit()
    conn.close()


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    ax.hist(x, bins=10)
    ax.set_title('test histogram')
    ax.set_xlabel('age')
    ax.set_ylabel('Num of Poeple')
    fig.show()

    plt.savefig("hoge.png") # この行を追記


get_agelist()
