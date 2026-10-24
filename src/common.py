from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
def load(name):
    return pd.read_csv(ROOT / "data" / f"{name}.csv")
