"""
models.py
Definición y entrenamiento de modelos de Scikit-Learn.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

def crear_modelo(tipo="random_forest", **kwargs):
    """
    Crea un modelo de ML según el tipo:
    - 'random_forest'
    - 'logistic_regression'
    - 'svm'
    kwargs permite pasar parámetros al modelo.
    """
    if tipo == "random_forest":
        model = RandomForestClassifier(**kwargs)
    elif tipo == "logistic_regression":
        model = LogisticRegression(max_iter=1000, **kwargs)
    elif tipo == "svm":
        model = SVC(**kwargs)
    else:
        raise ValueError("Tipo de modelo no soportado")
    return model

if __name__ == "__main__":
    # Ejemplo de uso
    modelo = crear_modelo("random_forest", n_estimators=50, random_state=42)
    print(modelo)
