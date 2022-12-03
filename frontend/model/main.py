import lightgbm as lgb
import pandas as pd
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from getData import read
import plotly.express as px



params = {

    "boosting_type": "gbdt",
    "objective": "regression",
    "metric":{'l2','l1'},
    "num_leaves": 30,
    "learning_rate": 0.07,
    "feature_fraction": 0.9,
    "bagging_fraction": .9,
    "bagging_freq": 9,
    "max_depth": 18,
    'feature_fraction': 0.97,
    'subsample': .2
}
train,validation,X_test,y_test,date=read('AllData\\trainingSets\\NVDA_SOXX_BTC.csv',1)



kant=lgb.train(params,train_set=train,valid_sets=validation,early_stopping_rounds=50,num_boost_round=2000)
#kant.score(testingD, testingL)
#print('Training accuracy {:.4f}'.format(kant.score(trainingD,trainingL)))
#print('Testing accuracy {:.4f}'.format(kant.score(testingD,testingL)))

df=pd.read_csv('AllData\\trainingSets\\NVDA_SOXX_BTC.csv')
df.drop(columns=['Date'], inplace=True)
for column in df.columns:
        df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())


dtrain = df.iloc[:int(len(df)*0.9),:]
#dtrain = dtrain.sample(frac=1, random_state=seed)


trainingD=dtrain.iloc[:int(len(df)*.75),1:]
trainingL=dtrain.iloc[:int(len(df)*.75),0]
validationD=dtrain.iloc[int(len(df)*.75):,1:]
validationL=dtrain.iloc[int(len(df)*.75):,0]
testingD=df.iloc[int(len(df)*0.9):,1:]
testingL=df.iloc[int(len(df)*0.9):,0]


x_all=df.iloc[:,1:]
y_all=df.iloc[:,0]
#y_pred = kant.predict(X_test, num_iteration=kant.best_iteration)
y_pred = kant.predict(x_all, num_iteration=kant.best_iteration)
#print(y_pred)
#print(sum(y_pred)/len(y_pred))
#print(sum(testingL)/len(testingL))
trp=kant.predict(trainingD, num_iteration=kant.best_iteration)
vp=kant.predict(validationD, num_iteration=kant.best_iteration)
te=kant.predict(testingD, num_iteration=kant.best_iteration)
print('MSE trp ',mean_squared_error(trainingL,trp))
print('MSE vp ',mean_squared_error(validationL,vp))
print('MSE te ',mean_squared_error(testingL,te))

print('MSE all: ',mean_squared_error(y_all,y_pred))
print(date)
print(date.shape)
#plt.plot(date, y_test, label = "Truth")
#plt.plot(date, y_pred, label = "Prediction")
#plt.legend()
#plt.show()

df=pd.DataFrame({'Date':date,'Truth':y_all,'Prediction':y_pred})
df.to_csv('AllData\\results\\NVDA_SOXX_BTC.csv', index=False)

#fig = px.line(df, x='Date', y=['Truth','Prediction'], title='Stock Price Prediction')
#fig.update_xaxes(rangeslider_visible=True)
#fig.show()
#ax = lgb.plot_importance(kant, max_num_features=10)
#plt.show()
#plt.show()