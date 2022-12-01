import lightgbm as lgb
import pandas as pd
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt
seed=1
df=pd.read_csv('AllData\\trainingSets\\NVDA_SOXX_BTC.csv')
df.drop(columns=['Date'], inplace=True)
#shuffle df based on seed
df=df.sample(frac=1, random_state=seed)

trainingD=df.iloc[:int(len(df)*0.8),1:]
trainingL=df.iloc[:int(len(df)*0.8),0]



testingD=df.iloc[int(len(df)*0.8):,1:]
testingL=df.iloc[int(len(df)*0.8):,0]


train_data = lgb.Dataset(trainingD, label=trainingL)

kant = lgb.LGBMRegressor()
kant.fit(trainingD, trainingL, verbose=20)
#kant.score(testingD, testingL)
print('Training accuracy {:.4f}'.format(kant.score(trainingD,trainingL)))
print('Testing accuracy {:.4f}'.format(kant.score(testingD,testingL)))

ax = lgb.plot_importance(kant, max_num_features=10)
plt.show()
#plt.show()