"""
metrics.py
Funciones para evaluar modelos de Machine Learning.
"""

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluar_modelo(y_true, y_pred):
    """
    Calcula métricas básicas de clasificación.
    Devuelve un diccionario con Accuracy, Precision, Recall y F1-score.
    """
    metrics = {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred, average='weighted'),
        "Recall": recall_score(y_true, y_pred, average='weighted'),
        "F1-score": f1_score(y_true, y_pred, average='weighted')
    }
    return metrics

if __name__ == "__main__":
    # Ejemplo rápido
    y_true = [0, 1, 2, 2, 1]
    y_pred = [0, 2, 2, 2, 1]
    resultados = evaluar_modelo(y_true, y_pred)
    print("Resultados de evaluación:\n", resultados)
