import pandas as pd
from sklearn.datasets import fetch_california_housing

def cargar_dataset():
    """Carga el dataset California Housing y devuelve X y y"""
    data = fetch_california_housing(as_frame=True)
    X = data.data
    y = data.target
    return X, y
