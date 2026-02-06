"""
preprocessing.py
Funciones para preprocesar datos antes del entrenamiento.
"""

from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
import pandas as pd

def escalar_datos(X, tipo="standard"):
    """
    Escala los datos numéricos:
    - 'standard': media 0, desviación 1
    - 'minmax': escala entre 0 y 1
    """
    if tipo == "standard":
        scaler = StandardScaler()
    elif tipo == "minmax":
        scaler = MinMaxScaler()
    else:
        raise ValueError("Tipo de escalado no soportado")
    X_scaled = scaler.fit_transform(X)
    return X_scaled

def codificar_labels(y):
    """
    Codifica etiquetas categóricas a números.
    """
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    return y_encoded

if __name__ == "__main__":
    # Ejemplo
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6]
    })
    print("Datos originales:\n", df)
    print("Datos escalados:\n", escalar_datos(df, "standard"))

    labels = ["rojo", "azul", "rojo"]
    print("Labels codificados:", codificar_labels(labels))
