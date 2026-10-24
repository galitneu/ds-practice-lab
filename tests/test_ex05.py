import numpy as np
import pandas as pd
import pytest
from src.api import exercise
from src.common import load
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_squared_error
from sklearn.dummy import DummyRegressor

def test_ex05_contract():
    frame = load("titanic"); fig = exercise(5).survival_plot(frame)
    ax = fig.axes[0]
    assert len(ax.patches) == 3
    assert np.allclose([p.get_height() for p in ax.patches],frame.groupby("pclass").survived.mean())
    assert ax.get_title() and ax.get_xlabel() and ax.get_ylabel()
    assert ax.get_ylim() == (0,1)
