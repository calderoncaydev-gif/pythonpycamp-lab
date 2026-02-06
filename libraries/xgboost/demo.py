from datasets import cargar_dataset
from models import entrenar_modelo

if __name__ == "__main__":
    X, y = cargar_dataset()
    model = entrenar_modelo(X, y)
