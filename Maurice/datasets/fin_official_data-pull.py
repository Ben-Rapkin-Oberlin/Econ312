
import pandas_datareader.data as web
import pandas as pd
import datetime

# Pulling all historical daily data for Nividia $NVDA
'''
start = datetime.datetime(1999,1,21)   
end = datetime.datetime(2022,10,30)
df = web.DataReader('NVDA', start = start, end = end, data_source='yahoo') # ['NVIDIA', 'SOXX', 'SEMI'] 
df = df.stack().reset_index()
'''
# Pulling all historical daily data for iShares Semiconductor ETF $SOXX
'''
df = web.DataReader('SOXX', start = start, end = end, data_source='yahoo') # ['NVDA', 'SOXX', 'SEMI'] 
df = df.stack().reset_index()
'''
# Pulling all historical daily data for Columbia Seligman Semiconductor & Technology ETF $SEMI
'''
df = web.DataReader('SEMI', start = start, end = end, data_source='yahoo') # ['NVDA', 'SOXX', 'SEMI'] 
df = df.stack().reset_index()
'''
# Pulling all historical daily data for Bitcoin BTC-USD
'''
df = web.DataReader('BTC-USD', start = start, end = end, data_source='yahoo') # ['NVDA', 'SOXX', 'SEMI', 'BTC-USD'] 
df = df.stack().reset_index()
'''
print(df)

df = df.to_csv('BTC-USD_historical.csv', encoding='utf-8', index=False)




'''
from locale import D_FMT
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import pandas_datareader.data as web
import datetime

'''