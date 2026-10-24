import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex06_contract():
    frame = load("titanic"); transformer = exercise(6).make_preprocessor()
    assert not hasattr(transformer,"transformers_")
    train = frame.iloc[:100]; test = frame.iloc[100:].copy(); test["embarked"] = "NEW_PORT"
    a = transformer.fit_transform(train); b = transformer.transform(test)
    assert a.shape[1] == b.shape[1] and b.shape[0] == len(test)
    assert np.isfinite(a.toarray() if hasattr(a,"toarray") else a).all()
    assert "survived" not in transformer.get_feature_names_out().tolist()
    assert not any("survived" in n or "alive" in n for n in transformer.get_feature_names_out())
    assert transformer.named_transformers_["numeric"].named_steps["impute"].statistics_[0] == train.age.median()
