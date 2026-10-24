import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex01_contract():
    frame = load("breast_cancer")
    result = exercise(1).profile(frame)
    assert result == {"rows": 569, "columns": 31, "missing": 0, "prevalence": frame.target.mean()}
    probe = frame.iloc[:9].copy(); probe.iloc[0, 0] = np.nan
    assert exercise(1).profile(probe)["missing"] == 1
