import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort
import pandas as pd
import json
import plotly
import plotly.express as px
from pathlib import Path, PureWindowsPath, PurePosixPath



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
def home():
    filename = PureWindowsPath('static\\gmeStock.png')
    correct_path = Path(filename)
    return render_template("home.html", user_image = correct_path)

@app.route('/financial')
def table():
    conn = get_db_connection()
    fin = conn.execute('SELECT * FROM fin').fetchall()
    conn.close()
    return render_template('table.html', title='Bootstrap Table',
                           fin=fin)
    #return render_template('index.html', monks1=monks1)

@app.route('/results')
def lineplot():
    filename = PureWindowsPath('results\\NVDA_SOXX_BTC_GBT.csv')
    correct_path = Path(filename)
    df = pd.read_csv(correct_path)
    fig = px.line(df, x='Date', y=['Truth','Prediction'], title='Gradient Boosted Tree')
    fig.add_vline(x=df.iloc[1832,0], line_width=3, line_dash="dash", line_color="black")
    fig.update_xaxes(rangeslider_visible=True)
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    

    filename = PureWindowsPath('results\\NVDA_SOXX_BTC_NN.csv')
    correct_path = Path(filename)
    df = pd.read_csv(correct_path)
    fig = px.line(df, x='Date', y=['Truth','Prediction'], title='Neural Network')
    fig.add_vline(x=df.iloc[1832,0], line_width=3, line_dash="dash", line_color="black")
    fig.update_xaxes(rangeslider_visible=True)
    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    filename=PureWindowsPath('results/MSE.csv')
    correct_path=Path(filename)
    mse=pd.read_csv(correct_path)
    df=pd.DataFrame({'Algorithm': ['GBT', 'NN'], 'Mean Squared Error' : [mse['GBTlimited'][0],mse['NNlimited'][0]]})
    fig = px.bar(df, x='Algorithm', y='Mean Squared Error', title='Comparative Accuracy', color='Algorithm')
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    #print(mse['GBT'][0])
    df=pd.DataFrame({'Algorithm': ['GBT', 'NN'], 'Mean Squared Error' : [mse['GBT'][0],mse['NN'][0]]})
    fig = px.bar(df, x='Algorithm', y='Mean Squared Error', title='Comparative Accuracy', color='Algorithm')
    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('lineplot.html', graphJSON1=graphJSON1, graphJSON2=graphJSON2, graphJSON3=graphJSON3, graphJSON4=graphJSON4)


@app.route('/methodology')
def methods():
    return render_template('methods.html')