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
X=df.iloc[int(len(df)*0.8):,1:].to_numpy()
Y=df.iloc[int(len(df)*0.8):,0].to_numpy()
test=df.iloc[:int(len(df)*0.8),1:].to_numpy()
testL=df.iloc[:int(len(df)*0.8),0].to_numpy()



import torch
import torch.nn as nn
import matplotlib.pyplot as plt

torch.manual_seed(1)    # reproducible

# torch can only train on Variable, so convert them to Variable
# The code below is deprecated in Pytorch 0.4. Now, autograd directly supports tensors
# x, y = Variable(x), Variable(y)

# plt.scatter(x.data.numpy(), y.data.numpy())
# plt.show()
class NeuralNetwork(torch.nn.Module):
    def __init__(self,datasize):
        super(NeuralNetwork, self).__init__()
        self.flatten = torch.nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            torch.nn.Linear(datasize, int(datasize/2)),
            torch.nn.ReLU(),
            torch.nn.Linear(int(datasize/2), int(datasize/4)),
            torch.nn.ReLU(),
            torch.nn.Linear(int(datasize/4), 1),
        )

    def forward(self, x):
        y = self.predict(x)
        return y


net = NeuralNetwork(X.shape[1])     # define the network
#print(net)  # net architecture

optimizer = torch.optim.SGD(net.parameters(), lr=0.2)
loss_func = torch.nn.MSELoss()  # this is for regression mean squared loss

plt.ion()   # something about plotting

for t in range(200):
    prediction = net(X)     # input x and predict based on x

    loss = loss_func(prediction, Y)     # must be (1. nn output, 2. target)

    optimizer.zero_grad()   # clear gradients for next train
    loss.backward()         # backpropagation, compute gradients
    optimizer.step()        # apply gradients

    if t % 5 == 0:
        # plot and show learning process
        plt.cla()
        plt.scatter(X.data.numpy(), Y.data.numpy())
        plt.plot(X.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color':  'red'})
        plt.pause(0.1)

plt.ioff()
plt.show()