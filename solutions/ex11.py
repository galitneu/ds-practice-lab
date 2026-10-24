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

def evaluate(y_true, probability, threshold=0.5):
    return {"roc_auc": roc_auc_score(y_true, probability), "pr_auc": average_precision_score(y_true, probability), "brier": brier_score_loss(y_true, probability), "confusion": confusion_matrix(y_true, np.asarray(probability) >= threshold, labels=[0, 1])}
