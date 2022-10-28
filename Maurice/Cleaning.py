
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('btcusd.csv')
start_date = pd.to_datetime('2020-1-31')
end_date = pd.to_datetime('2022-10-25')                         
df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
stock_data = df1.set_index('Date')
top_plt = plt.subplot2grid((5,4), (0, 0), rowspan=3, colspan=4)
top_plt.plot(stock_data.index, stock_data['Close (USD)'])
plt.title('BTC/USD [31-1-2020 to 25-10-2022]')
bottom_plt = plt.subplot2grid((5,4), (3,0), rowspan=1, colspan=4)
bottom_plt.bar(stock_data.index, stock_data['Volume'])
plt.title('\nBTC/USD Trading Volume', y=-0.60)
plt.gcf().set_size_inches(12,8)

'''
df = pd.read_csv('btcusd.csv')
print(df)

pd.read_csv('btcusd.csv', sep='\t')
'''
