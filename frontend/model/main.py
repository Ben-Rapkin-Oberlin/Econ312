import lightgbm as lgb
import pandas as pd
import numpy as np
seed=1
df=pd.read_csv('AllData\\trainingSets\\NVDA_SOXX_BTC.csv')
#shuffle df based on seed
df=df.sample(frac=1, random_state=seed)

trainingD=df.iloc[:int(len(df)*0.6),1:].to_numpy
trainingL=df.iloc[:int(len(df)*0.6),0].to_numpy

validationD=df.iloc[int(len(df)*0.6):int(len(df)*0.8),1:].to_numpy
validationL=df.iloc[int(len(df)*0.6):int(len(df)*0.8),0].to_numpy

validation_data = lgb.Dataset('validation.svm', reference=train_data)
testingD=df.iloc[int(len(df)*0.8):,:].to_numpy
testingL=df.iloc[int(len(df)*0.8):,0].to_numpy


train_data = lgb.Dataset(trainingD, label=trainingL)
validation_data = train_data.create_valid(), label=validationL)

