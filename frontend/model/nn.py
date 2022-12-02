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


Import torch
import torch.nn as nn
import torch.nn.functional as F

class NeuralNetwork(nn.Module):
    def __init__(self,datasize):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(datasize, int(datasize/2)),
            nn.ReLU(),
            nn.Linear(int(datasize/2), int(datasize/4)),
            nn.ReLU(),
            nn.Linear(int(datasize/4), 1),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
model = NeuralNetwork(x.shape[1])
james=X)

#print(mean_squared_error(predictions,testL))
plt.plot(testL.index, testL, label = "Truth")
plt.plot(testL.index, predictions, label = "Prediction")
plt.legend()
plt.show()




   #an array of predictions, of shape 1xinstances, retains order

   