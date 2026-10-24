import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex09_contract():
    frame = load("breast_cancer")
    a,b,c,d = train_test_split(frame.drop(columns="target"),frame.target,test_size=.25,stratify=frame.target,random_state=42)
    model = exercise(9).make_forest(); model.fit(a,c)
    assert roc_auc_score(d,model.predict_proba(b)[:,1]) > .95
    assert model[-1].n_estimators == 120 and model[-1].min_samples_leaf == 2
