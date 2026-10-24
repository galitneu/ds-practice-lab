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

def clean(frame):
    result = frame.drop_duplicates("patient_id").copy()
    for column, low, high in [("age", 18, 100), ("bmi", 10, 70)]:
        values = pd.to_numeric(result[column], errors="coerce")
        values = values.where(values.between(low, high))
        result[column] = values.fillna(values.median())
    result["sex"] = result.sex.str.strip().str.lower().replace({"f": "female", "m": "male"}).fillna("unknown")
    result["sex"] = result.sex.where(result.sex.isin(["female", "male"]), "unknown")
    return result
