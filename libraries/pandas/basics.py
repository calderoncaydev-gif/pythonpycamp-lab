"""
basic.py
Operaciones simples con DataFrames y Series.
"""

import pandas as pd

def mostrar_informacion(df):
    """Muestra información general del DataFrame."""
    print("Info del DataFrame:")
    print(df.info())
    print("\nDescripción estadística:")
    print(df.describe())

def seleccionar_columnas(df, columnas):
    """Selecciona columnas específicas del DataFrame."""
    return df[columnas]

def filtrar_por_condicion(df, columna, valor):
    """Filtra filas donde columna == valor"""
    return df[df[columna] == valor]

if __name__ == "__main__":
    data = {
        'Nombre': ['Ana', 'Luis', 'Carla', 'Juan'],
        'Edad': [23, 35, 29, 41],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
    }
    df = pd.DataFrame(data)
    
    mostrar_informacion(df)
    print("\nSeleccionar columnas Nombre y Edad:\n", seleccionar_columnas(df, ['Nombre', 'Edad']))
    print("\nFiltrar Ciudad == Sevilla:\n", filtrar_por_condicion(df, 'Ciudad', 'Sevilla'))
