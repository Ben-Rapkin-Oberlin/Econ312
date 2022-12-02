import pandas as pd
import lightgbm as lgb
import matplotlib.pyplot as plt

def read(path,seed):
    seed=1
    df=pd.read_csv(path)
    temp=df['Date']
    temp=temp.iloc[int(len(df)*0.8):]
    df.drop(columns=['Date'], inplace=True)
    a=df.columns
    a=a[1:]
    plt.plot(df.index, df['open_NVDA'], label = "truth")
    plt.legend()
    plt.show()

    for column in a:
        df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    #shuffle df based on seed
    dtrain = df.iloc[:int(len(df)*0.8),:]
    dtrain = dtrain.sample(frac=1, random_state=seed)


    trainingD=dtrain.iloc[:int(len(df)*.75),1:]
    trainingL=dtrain.iloc[:int(len(df)*.75),0]

    validationD=df.iloc[int(len(df)*0.6):int(len(df)*0.75):,1:]
    validationL=df.iloc[int(len(df)*0.6):int(len(df)*0.75):,0]



    testingD=df.iloc[int(len(df)*0.8):,1:]
    testingL=df.iloc[int(len(df)*0.8):,0]


    train_data = lgb.Dataset(trainingD, label=trainingL)
    validation=lgb.Dataset(validationD, label=validationL,reference=train_data)

    return train_data,validation,testingD,testingL,temp