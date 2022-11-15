import pandas_datareader.data as pdr
import pandas as pd
import datetime

# Industrial Production: Durable Goods Materials: Semiconductors, Printed Circuit Boards, and Other,  Producer Price Index by Industry: Semiconductor and Other Electronic Component Manufacturing, Personal Consumption Expenditures: Nondurable Goods, and  Personal Consumption Expenditures

start = datetime.datetime(1900,1,1)   
end = datetime.datetime.now()
'''
df = pdr.DataReader('IPB53122S', start = start, end = end, data_source='fred') # ['IPB53122S', 'PCU33443344', 'PCEND', 'PCE'] 
'''
'''
df = pdr.DataReader('PCU33443344', start = start, end = end, data_source='fred') # ['IPB53122S', 'PCU33443344', 'PCEND', 'PCE'] 
df = df.stack().reset_index()
print(df)
'''
df = pdr.DataReader('PCE', start = start, end = end, data_source='fred') # ['IPB53122S', 'PCU33443344', 'PCEND', 'PCE'] 
df = df.stack().reset_index()
print(df)
df = df.to_csv('PCE_historical.csv', encoding='utf-8', index=False)
