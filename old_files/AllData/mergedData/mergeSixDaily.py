import pandas as pd

data1999 = pd.read_csv("datasets/economic/NVDA_historical.csv")
data2001 = pd.read_csv("datasets/economic/SOXX_historical.csv")

# both of these are daily data but distrubuted over 6 rows

#high,low,open,close,volume,adjclose
d1=data1999[::6].copy(deep=True)
d1.rename(columns={"0": "high"}, inplace=True)
d1=d1.drop(columns=['level_1'])

d2=data1999[1::6].copy(deep=True)
d2.rename(columns={"0": "low"}, inplace=True)
d2=d2.drop(columns=['level_1'])

d3=data1999[2::6].copy(deep=True)
d3.rename(columns={"0": "open"}, inplace=True)
d3=d3.drop(columns=['level_1'])

d4=data1999[3::6].copy(deep=True)
d4.rename(columns={"0": "close"}, inplace=True)
d4=d4.drop(columns=['level_1'])

d5=data1999[4::6].copy(deep=True)
d5.rename(columns={"0": "volume"}, inplace=True)
d5=d5.drop(columns=['level_1'])

d6=data1999[5::6].copy(deep=True)
d6.rename(columns={"0": "adjclose"}, inplace=True)
d6=d6.drop(columns=['level_1'])

d1=pd.merge(d1, d2, on='Date')
d3=pd.merge(d3, d4, on='Date')
d5=pd.merge(d5, d6, on='Date')
d1=pd.merge(d1, d3, on='Date')
d1=pd.merge(d1, d5, on='Date')

d1.to_csv("mergedData/NVDA.csv", index=False)

d1=data2001[::6].copy(deep=True)
d1.rename(columns={"0": "high"}, inplace=True)
d1=d1.drop(columns=['level_1'])

d2=data2001[1::6].copy(deep=True)
d2.rename(columns={"0": "low"}, inplace=True)
d2=d2.drop(columns=['level_1'])

d3=data2001[2::6].copy(deep=True)
d3.rename(columns={"0": "open"}, inplace=True)
d3=d3.drop(columns=['level_1'])

d4=data2001[3::6].copy(deep=True)
d4.rename(columns={"0": "close"}, inplace=True)
d4=d4.drop(columns=['level_1'])

d5=data2001[4::6].copy(deep=True)
d5.rename(columns={"0": "volume"}, inplace=True)
d5=d5.drop(columns=['level_1'])

d6=data2001[5::6].copy(deep=True)
d6.rename(columns={"0": "adjclose"}, inplace=True)
d6=d6.drop(columns=['level_1'])

d1=pd.merge(d1, d2, on='Date')
d3=pd.merge(d3, d4, on='Date')
d5=pd.merge(d5, d6, on='Date')
d1=pd.merge(d1, d3, on='Date')
d1=pd.merge(d1, d5, on='Date')

d1.to_csv("mergedData/SOXX.csv", index=False)
