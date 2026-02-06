import pandas as pd
from sklearn.datasets import load_diabetes

def cargar_dataset():
    """Carga dataset de ejemplo y devuelve X y y"""
    data = load_diabetes()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="Target")
    return X, y
