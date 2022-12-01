import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_data(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/financial')
def table():
    conn = get_db_connection()
    monks1 = conn.execute('SELECT * FROM monks1').fetchall()
    conn.close()
    return render_template('table.html', title='Bootstrap Table',
                           monks1=monks1)
    #return render_template('index.html', monks1=monks1)