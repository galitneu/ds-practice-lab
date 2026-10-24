import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex03_contract():
    frame = load("pima"); result = exercise(3).summarize(frame)
    assert list(result.columns) == ["mean","median","missing_rate"]
    assert result.loc["glucose","missing_rate"] == (frame.glucose == 0).mean()
    assert result.loc["pregnancies","median"] == frame.pregnancies.median()
    assert result.loc["bmi","mean"] == pytest.approx(frame.bmi.replace(0,np.nan).mean())
