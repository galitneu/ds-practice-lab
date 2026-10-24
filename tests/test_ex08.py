import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex08_contract():
    frame = load("breast_cancer")
    a,b,c,d = train_test_split(frame.drop(columns="target"),frame.target,test_size=.25,stratify=frame.target,random_state=42)
    model = exercise(8).make_model()
    assert not hasattr(model[-1],"classes_")
    model.fit(a,c)
    assert roc_auc_score(d,model.predict_proba(b)[:,1]) > .95
    assert np.allclose(model["impute"].statistics_,a.median())
    assert np.allclose(model["scale"].mean_,a.mean())
