import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex11_contract():
    result = exercise(11).evaluate([0,0,0,1],[.1,.4,.8,.7],threshold=.75)
    assert result["roc_auc"] == pytest.approx(2/3)
    assert result["pr_auc"] == pytest.approx(.5)
    assert result["brier"] == pytest.approx(.225)
    assert np.array_equal(result["confusion"],[[2,1],[1,0]])
    assert exercise(11).evaluate([0,1],[.1,.5])["confusion"][1,1] == 1
