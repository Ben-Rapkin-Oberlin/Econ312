from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import plotly.express as px
from pathlib import Path, PureWindowsPath


def read(path,seed):
    seed=1
    df=pd.read_csv(path)
    temp=df['Date']
    #temp=temp.iloc[int(len(df)*0.8):]
    df.drop(columns=['Date'], inplace=True)
    a=df.columns
    #a=a[1:]
    #plt.plot(df.index, df['open_NVDA'], label = "truth")
    #plt.legend()
    #plt.show()

    for column in a:
        df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    #shuffle df based on seed
    dtrain = df.iloc[:int(len(df)*0.9),:]
    dtrain = dtrain.sample(frac=1, random_state=seed)


    trainingD=dtrain.iloc[:int(len(df)*.75),1:]
    trainingL=dtrain.iloc[:int(len(df)*.75),0]

    validationD=df.iloc[int(len(df)*0.6):int(len(df)*0.75):,1:]
    validationL=df.iloc[int(len(df)*0.6):int(len(df)*0.75):,0]



    testingD=df.iloc[int(len(df)*0.9):,1:]
    testingL=df.iloc[int(len(df)*0.9):,0]
    return trainingD,trainingL,validationD,validationL,testingD,testingL,temp

filename = PureWindowsPath('model\\NVDA_SOXX_BTC.csv')
correct_path = Path(filename)
X,Y,vx,vy,test,testL,date=read(correct_path,1)

#data is a pandas dataframe
#col 0 is labels
#print("#####Neural Network#####")


regr = MLPRegressor(random_state=1, max_iter=500).fit(X, Y)

filename = PureWindowsPath('model\\NVDA_SOXX_BTC.csv')
correct_path = Path(filename)
df=pd.read_csv(correct_path)
df.drop(columns=['Date'], inplace=True)
for column in df.columns:
        df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())

x_all=df.iloc[:,1:]
y_all=df.iloc[:,0]




pred=regr.predict(x_all)

print(mean_squared_error(y_all,pred))
df=pd.DataFrame({'Date':date,'Truth':y_all,'Prediction':pred})

filename = PureWindowsPath('results\\NVDA_SOXX_BTC_NN.csv')
correct_path = Path(filename)
df.to_csv(correct_path, index=False)

