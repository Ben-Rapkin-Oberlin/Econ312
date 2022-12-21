import pandas as pd

"""df=pd.read_csv('tweets.csv')
a=df.columns.tolist()
a.insert(0, a[2])
a.pop(3)
df=df[a]
print(df.columns)
print(df.shape)
df.to_csv('tweets.csv', index=False)"""

df1=pd.read_csv('tweets.csv')

df1=df1.rename(columns={'Datetime': 'Date'})
print(df1.columns[0])
print(df1.shape)
df2=pd.read_csv('NVDA_SOXX_BTC.csv')
print(df2.shape)
df=pd.merge(df1, df2, on='Date', how='inner')
print(df.columns)
print(df.shape)
print(df.head())
df.to_csv('combined.csv', index=False)


