import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex12_contract():
    frame = load("california"); X = frame.drop(columns="median_house_value"); y = frame.median_house_value
    a,b,c,d = train_test_split(X,y,test_size=.25,random_state=42)
    model = exercise(12).make_regressor(); model.fit(a,c)
    baseline = DummyRegressor().fit(a,c)
    assert mean_squared_error(d,model.predict(b))**.5 < .85 * mean_squared_error(d,baseline.predict(b))**.5
    assert np.allclose(model["impute"].statistics_,a.median())
