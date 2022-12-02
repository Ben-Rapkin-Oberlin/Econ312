import lightgbm as lgb
import pandas as pd
import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from getData import read


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

y_pred = kant.predict(X_test, num_iteration=kant.best_iteration)
#print(y_pred)
#print(sum(y_pred)/len(y_pred))
#print(sum(testingL)/len(testingL))
print(mean_squared_error(y_test,y_pred))
print(date)
print(date.shape)
plt.plot(date, y_test, label = "Truth")
plt.plot(date, y_pred, label = "Prediction")
plt.legend()
plt.show()


#ax = lgb.plot_importance(kant, max_num_features=10)
#plt.show()
#plt.show()