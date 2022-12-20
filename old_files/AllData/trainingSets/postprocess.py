import pandas as pd

df=pd.read_csv('AllData\\trainingSets\\NVDA_SOXX_BTC.csv')

new=df.columns.tolist()
print(new)
new=[x.replace('.','') for x in new]
df.columns = new
#print(df.head())
#this is because we can't see the future and know how those stocks will preform at the end of the day
df.drop(columns=['high_SOXX','low_SOXX','close_SOXX','volume_SOXX','adjclose_SOXX',
            'high_BTC','low_BTC','close_BTC','volume_BTC','adjclose_BTC',
            'low_NVDA','high_NVDA','close_NVDA','volume_NVDA','adjclose_NVDA' ], inplace=True)
df.to_csv('AllData\\trainingSets\\NVDA_SOXX_BTC.csv', index=False)

 