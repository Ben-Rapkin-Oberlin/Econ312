#let tree see past five days of information

import pandas as pd

df=pd.read_csv('AllData\\mergedData\\semi-final\\NVDA_SOXX_BTC.csv')
temp=df.loc[8:,'Date']
temp=temp.reset_index(drop=True)

print(temp.head()   )
#remove first five rows as we want one key for each day
df=df.drop(columns=['Date'])

final=pd.DataFrame(pd.concat([df.iloc[0,:], df.iloc[1,:], df.iloc[2,:], df.iloc[3,:], 
                    df.iloc[4,:], df.iloc[5,:], df.iloc[6,:], df.iloc[7,:], df.iloc[8,:]], axis=0))

#final=pd.concat([df.iloc[0,:], df.iloc[1,:]], axis=0)
#print(df.iloc[0,:]+df.iloc[1,:])



print("#"*50)
for i in range (1,len (df)-8):
    a=pd.concat([df.iloc[i,:], df.iloc[i+1,:], df.iloc[i+2,:], df.iloc[i+3,:], 
    df.iloc[i+4,:] , df.iloc[i+5,:], df.iloc[i+6,:], df.iloc[i+7,:], df.iloc[i+8,:]], axis=0)
    final=pd.concat([final, a], axis=1)    
final=final.T.reset_index(drop=True)
print(final.head())
#exit()
final=pd.merge(temp,final, how='right', left_index=True, right_index=True)
#final=final.drop(columns=['Date'])
#print(final.shape)
#print(final.head())
final.to_csv('AllData\\trainingSets\\NVDA_SOXX_BTC.csv', index=False)