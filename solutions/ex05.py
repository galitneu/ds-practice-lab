import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss, confusion_matrix

def survival_plot(frame):
    rates = frame.groupby("pclass").survived.mean().sort_index()
    fig, ax = plt.subplots()
    ax.bar(rates.index.astype(str), rates.values)
    ax.set(title="Observed survival by passenger class", xlabel="Passenger class", ylabel="Survival proportion", ylim=(0, 1))
    return fig
