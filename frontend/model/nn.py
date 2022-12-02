from sklearn.neural_network import MLPClassifier
import pandas as pd
from warnings import simplefilter
from sklearn.exceptions import ConvergenceWarning
simplefilter("ignore", category=ConvergenceWarning)
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import time
#from getData import read

df=pd.read_csv('AllData\\trainingSets\\NVDA_SOXX_BTC.csv')
#data is a pandas dataframe
#col 0 is labels
#print("#####Neural Network#####")
df=df.drop(columns=['Date'])
x=df.iloc[int(len(df)*0.8):,1:].to_numpy()
y=df.iloc[int(len(df)*0.8):,0].to_numpy()
test=df.iloc[:int(len(df)*0.8),1:].to_numpy()
testL=df.iloc[:int(len(df)*0.8),0].to_numpy()
#print(testL)
Diego = MLPClassifier(random_state=1)

#MLPClassifier(solver='lbfgs', alpha=1e-5,
 #hidden_layer_sizes=(50,), random_state=1,max_iter=100)

#st=time.process_time()
Diego.fit(x,y)
#print(time.process_time()-st)
predictions=Diego.predict(test) 
#print(mean_squared_error(predictions,testL))
plt.plot(testL.index, testL, label = "Truth")
plt.plot(testL.index, predictions, label = "Prediction")
plt.legend()
plt.show()




   #an array of predictions, of shape 1xinstances, retains order

   