import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex10_contract():
    frame = load("breast_cancer")
    a,b,c,d = train_test_split(frame.drop(columns="target"),frame.target,test_size=.25,stratify=frame.target,random_state=42)
    search = exercise(10).make_search()
    assert search.scoring == "roc_auc" and search.cv.n_splits == 4
    assert search.cv.shuffle and search.cv.random_state == 42
    assert search.param_grid == {"model__C":[.1,1,10]}
    search.fit(a,c)
    assert search.best_score_ > .95
    assert roc_auc_score(d, search.predict_proba(b)[:,1]) > .95
    assert np.allclose(search.best_estimator_["impute"].statistics_,a.median())
