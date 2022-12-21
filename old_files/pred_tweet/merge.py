import pandas as pd
import os 
df=pd.DataFrame()
paths=os.listdir()
df=pd.read_csv(paths[0])
df=df.rename(columns={"Mean":"Mean_"+paths[0][:-4],"SD":"SD_"+paths[0][:-4]})
#print(df.columns)
path=paths[1:]

for path in paths:
    if path.endswith(".csv"):
        df1=pd.read_csv(path)
        df1=df1.rename(columns={"Mean":"Mean_"+path[:-4],"SD":"SD_"+path[:-4]})
        #print(df1.shape)
        #print(df.shape)
        df=pd.merge(df,df1,on="Datetime",how="outer")
        #print(df.shape)
        #print(df.head)

#for i in df.columns:
#    df[i]=df[i].fillna(
 #   train_df['LoanAmount'] = train_df['LoanAmount'].fillna(train_df['LoanAmount'].mean())
df=df.fillna(method='ffill')
print(df.columns)
print(df.shape)
print(df.head())
print(df["Mean_gpu_tweets"])
df.to_csv("../../frontend/model/tweets.csv",index=False)

