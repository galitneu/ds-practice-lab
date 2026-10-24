import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex07_contract():
    frame = load("breast_cancer"); frame["leaked_target"] = frame.target
    Xtr,Xte,ytr,yte = exercise(7).split(frame)
    assert len(Xte) == 143 and len(Xtr) == 426
    assert set(Xtr.index).isdisjoint(Xte.index)
    assert set(Xtr.index) | set(Xte.index) == set(frame.index)
    assert "target" not in Xtr and "leaked_target" not in Xtr
    assert abs(ytr.mean()-yte.mean()) < .02
    pd.testing.assert_series_equal(ytr,frame.target.loc[Xtr.index])
