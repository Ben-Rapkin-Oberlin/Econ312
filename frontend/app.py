import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort
import pandas as pd
import json
import plotly
import plotly.express as px
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
    fin = conn.execute('SELECT * FROM fin').fetchall()
    conn.close()
    return render_template('table.html', title='Bootstrap Table',
                           fin=fin)
    #return render_template('index.html', monks1=monks1)

@app.route('/models')
def lineplot():
    df = pd.read_csv('AllData\\results\\NVDA_SOXX_BTC.csv')
    fig = px.line(df, x='Date', y=['Truth','Prediction'], title='Stock Price Prediction')
    fig.add_vline(x=df.iloc[1832,0], line_width=3, line_dash="dash", line_color="black")
    fig.update_xaxes(rangeslider_visible=True)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('lineplot.html', graphJSON=graphJSON)