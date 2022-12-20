import pandas as pd

# Read in the data'
#not useing BTC as there is too little data, only 1 year
#dfBTC=pd.read_csv('datasets\\economic\\BTC-USD.csv')
dfNVDA=pd.read_csv('mergedData\\NVDA.csv')
dfSOXX=pd.read_csv('mergedData\\SOXX.csv')


#dfBTC.rename(columns={'High':'high', "low":'low', 'Open':'open','Adj Close': 'adjclose'}, inplace=True)
#dfBTC.rename(columns={'Close':'close', 'Low':'low', 'Volume':'volume'}, inplace=True)
#print(df.columns)

#print(dfBTC[0:2])
print(dfNVDA.shape)
print(dfSOXX.shape)

#5982 - 5359 = 623

#dfBTC=dfBTC[0:623]
dfNVDA=dfNVDA[623:].reset_index(drop=True)

print(dfNVDA[0:2])
print(dfSOXX[0:2])

df=pd.merge(dfNVDA, dfSOXX, on='Date', how='inner', suffixes=('_NVDA', '_SOXX'))
print(df.shape)
print(df[0:2])

df.to_csv('mergedData\\semi-final\\NVDA_SOXX.csv', index=False)

