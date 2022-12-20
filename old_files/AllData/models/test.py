# coding: utf-8
from pathlib import Path

import pandas as pd

import lightgbm as lgb

if lgb.compat.MATPLOTLIB_INSTALLED:
    import matplotlib.pyplot as plt
else:
    raise ImportError('You need to install matplotlib and restart your session for plot_example.py.')

print('Loading data...')
# load or create your dataset

df=pd.read_csv('AllData\\trainingSets\\NVDA_SOXX_BTC.csv')
df.drop(columns=['Date'], inplace=True)
X_train=df.iloc[:int(len(df)*0.8),1:]
y_train=df.iloc[:int(len(df)*0.8),0]

X_test=df.iloc[int(len(df)*0.8):,1:]
y_test=df.iloc[int(len(df)*0.8):,0]


# create dataset for lightgbm
lgb_train = lgb.Dataset(X_train, y_train)
lgb_test = lgb.Dataset(X_test, y_test, reference=lgb_train)

# specify your configurations as a dict
params = {
    'num_leaves': 5,
    'metric': ('l1', 'l2'),
    'verbose': 0
}

evals_result = {}  # to record eval results for plotting

print('Starting training...')
# train
gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=100,
    valid_sets=[lgb_train, lgb_test],
    feature_name=[f'f{i + 1}' for i in range(X_train.shape[-1])],
    categorical_feature=[21],
    callbacks=[
        lgb.log_evaluation(10),
        lgb.record_evaluation(evals_result)
    ]
)

print('Plotting metrics recorded during training...')
ax = lgb.plot_metric(evals_result, metric='l1')
plt.show()

print('Plotting feature importances...')
ax = lgb.plot_importance(gbm, max_num_features=10)
plt.show()

print('Plotting split value histogram...')
ax = lgb.plot_split_value_histogram(gbm, feature='f26', bins='auto')
plt.show()

print('Plotting 54th tree...')  # one tree use categorical feature to split
ax = lgb.plot_tree(gbm, tree_index=53, figsize=(15, 15), show_info=['split_gain'])
plt.show()

print('Plotting 54th tree with graphviz...')
graph = lgb.create_tree_digraph(gbm, tree_index=53, name='Tree54')
graph.render(view=True)