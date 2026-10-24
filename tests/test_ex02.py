import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex02_contract():
    frame = load("messy_health"); original = frame.copy(deep=True)
    result = exercise(2).clean(frame)
    assert len(result) == 200 and result.patient_id.is_unique
    assert result.isna().sum().sum() == 0
    assert result.age.between(18,100).all() and result.bmi.between(10,70).all()
    assert set(result.sex) <= {"female", "male", "unknown"}
    assert pd.api.types.is_numeric_dtype(result.age)
    pd.testing.assert_frame_equal(frame, original)
    probe = pd.DataFrame({"patient_id":[1,2,3,3], "age":["20","40","bad","bad"], "bmi":[20,40,999,999], "sex":[" F ","M",None,None], "outcome":[0,1,0,0]})
    clean = exercise(2).clean(probe)
    assert clean.age.iloc[2] == 30 and clean.bmi.iloc[2] == 30
    assert clean.sex.tolist() == ["female","male","unknown"]
