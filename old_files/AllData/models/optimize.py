from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
import skopt
import neptunecontrib
import lightgbm as lgb
import pandas as pd
import neptune
import skopt
import sys
import os
from getData import read

SEARCH_PARAMS = {'learning_rate': 0.4,
                'max_depth': 15,
                'num_leaves': 32,
                'feature_fraction': 0.8,
                'subsample': 0.2}

FIXED_PARAMS={'objective': 'binary',
             'metric': 'auc',
             'is_unbalance':True,
             'bagging_freq':5,
             'boosting':'dart',
             'num_boost_round':300,
             'early_stopping_rounds':30}

train_data,valid_data,X_test,y_test=read('AllData\\trainingSets\\NVDA_SOXX_BTC.csv',1)

def train_evaluate(search_params):


   params = {'metric':FIXED_PARAMS['metric'],
             'objective':FIXED_PARAMS['objective'],
             **search_params}

   model = lgb.train(params, train_data,
                     valid_sets=[valid_data],
                     num_boost_round=FIXED_PARAMS['num_boost_round'],
                     early_stopping_rounds=FIXED_PARAMS['early_stopping_rounds'],
                     valid_names=['valid'])
   score = model.best_score['valid']['auc']
   return score

neptune.init('testest/LightGBM-hyperparameters')
neptune.create_experiment('lgb-tuning_final', upload_source_files=['*.*'],
                              tags=['lgb-tuning', 'dart'],params=SEARCH_PARAMS)

SPACE = [
   skopt.space.Real(0.01, 0.5, name='learning_rate', prior='log-uniform'),
   skopt.space.Integer(1, 30, name='max_depth'),
   skopt.space.Integer(10, 200, name='num_leaves'),
   skopt.space.Real(0.1, 1.0, name='feature_fraction', prior='uniform'),
   skopt.space.Real(0.1, 1.0, name='subsample', prior='uniform')
]
@skopt.utils.use_named_args(SPACE)
def objective(**params):
   return -1.0 * train_evaluate(params)

monitor = neptunecontrib.monitoring.skopt.NeptuneMonitor()
results = skopt.forest_minimize(objective, SPACE,
                                n_calls=100, n_random_starts=10,
                                callback=[monitor])
neptunecontrib.monitoring.skopt.log_results(results)

neptune.stop()