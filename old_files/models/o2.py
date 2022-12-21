import lightgbm as lgb
import neptune.new as neptune
import numpy as np
from neptune.new.integrations.lightgbm import (
    NeptuneCallback, create_booster_summary
)
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from getData import read

# Create run
run = neptune.init_run(
    project="common/lightgbm-integration",
    api_token=neptune.ANONYMOUS_API_TOKEN,
    name="train-cls",
    tags=["lgbm-integration", "train", "cls"],
)

# Create Neptune callback
neptune_callback = NeptuneCallback(run=run)

lgb_train,lgb_eval,X_test,y_test=read('AllData\\trainingSets\\NVDA_SOXX_BTC.csv',1)


# Define parameters
params = {

    "boosting_type": "gbdt",
    "objective": "regression",
    "metric":{'l2','l1'},
    "num_leaves": 21,
    "learning_rate": 0.05,
    "feature_fraction": 0.9,
    "bagging_fraction": 0.8,
    "bagging_freq": 5,
    "max_depth": 12,
}

# Train the model
gbm = lgb.train(
    params,
    lgb_train,
    num_boost_round=200,
    valid_sets=[lgb_train, lgb_eval],
    valid_names=["training", "validation"],
    callbacks=[neptune_callback],
)

y_pred = np.argmax(gbm.predict(X_test))

# Log summary metadata to the same run under the "lgbm_summary" namespace
run["lgbm_summary"] = create_booster_summary(
    booster=gbm,
    log_trees=True,
    list_trees=[0, 1, 2, 3, 4],
    log_confusion_matrix=True,
    y_pred=y_pred,
    y_true=y_test,
)

# When done logging, stop the run
run.stop()
