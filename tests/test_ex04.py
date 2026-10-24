import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex04_contract():
    frame = load("heart"); frame["note"] = "category"
    result = exercise(4).correlations(frame)
    pd.testing.assert_frame_equal(result,frame.select_dtypes(include="number").corr(method="spearman"))
