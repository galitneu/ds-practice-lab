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

def summarize(frame):
    result = frame.copy()
    columns = ["glucose", "blood_pressure", "skin_thickness", "insulin", "bmi"]
    result[columns] = result[columns].replace(0, np.nan)
    return pd.DataFrame({"mean": result.mean(), "median": result.median(), "missing_rate": result.isna().mean()})
