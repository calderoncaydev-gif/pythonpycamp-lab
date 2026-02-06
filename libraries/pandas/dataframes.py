"""
dataframes.py
Funciones para crear DataFrames de Pandas.
"""

import pandas as pd
import numpy as np  # Importamos NumPy directamente

def crear_dataframe_basico():
    """Crea un DataFrame simple a partir de un diccionario."""
    data = {
        'Nombre': ['Ana', 'Luis', 'Carla', 'Juan'],
        'Edad': [23, 35, 29, 41],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
    }
    df = pd.DataFrame(data)
    return df

def crear_dataframe_aleatorio(filas=5, columnas=3):
    """Crea un DataFrame con números aleatorios."""
    df = pd.DataFrame(
        np.random.randint(0, 100, size=(filas, columnas)),  # Usamos np.random.randint
        columns=[f'Col{i+1}' for i in range(columnas)]
    )
    return df

if __name__ == "__main__":
    df = crear_dataframe_basico()
    print("DataFrame básico:\n", df)

    df_rand = crear_dataframe_aleatorio()
    print("\nDataFrame aleatorio:\n", df_rand)
