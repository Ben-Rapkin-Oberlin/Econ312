import pandas  as  pd

df= pd.read_csv('C:\\Users\\benra\\Documents\\Academics\\fall 22\\312\\Econ312\\frontend\\AllData\\datasets\\economic\\BTC-USD_historical.csv')
df=df.iloc[:,0:3]
d1=df[::6].copy(deep=True)
d1.rename(columns={"0": "high_BTC"}, inplace=True)
d1=d1.drop(columns=['level_1'])

d2=df[1::6].copy(deep=True)
d2.rename(columns={"0": "low_BTC"}, inplace=True)
d2=d2.drop(columns=['level_1'])

d3=df[2::6].copy(deep=True)
d3.rename(columns={"0": "open_BTC"}, inplace=True)
d3=d3.drop(columns=['level_1'])

d4=df[3::6].copy(deep=True)
d4.rename(columns={"0": "close_BTC"}, inplace=True)
d4=d4.drop(columns=['level_1'])

d5=df[4::6].copy(deep=True)
d5.rename(columns={"0": "volume_BTC"}, inplace=True)
d5=d5.drop(columns=['level_1'])

d6=df[5::6].copy(deep=True)
d6.rename(columns={"0": "adjclose_BTC"}, inplace=True)
d6=d6.drop(columns=['level_1'])


d1=pd.merge(d1, d2, on='Date')
d3=pd.merge(d3, d4, on='Date')
d5=pd.merge(d5, d6, on='Date')
d1=pd.merge(d1, d3, on='Date')
d1=pd.merge(d1, d5, on='Date')

#now fix date
for i in range(len(d1)):
    s=d1.iloc[i,0].split('-')
    if len(s[1])==1:
        s[1]='0'+s[1]
    if len(s[0])==1:
        s[0]='0'+s[0]
    d1.iloc[i,0]='20'+s[2]+'-'+s[0]+'-'+s[1]
   
new=pd.read_csv('AllData\\mergedData\\semi-final\\NVDA_SOXX.csv')
new=new[3315:]  

df=pd.merge(new, d1, on='Date', how='inner')
    
print(df.shape)
print(df[0:2])

df.to_csv('AllData\\mergedData\\semi-final\\NVDA_SOXX_BTC.csv', index=False)
#5359-2966=2393