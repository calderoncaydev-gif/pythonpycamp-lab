"""
operations.py
Operaciones más avanzadas con DataFrames.
"""

import pandas as pd

def agregar_columna(df, nombre_columna, valores):
    """Agrega una nueva columna al DataFrame"""
    df[nombre_columna] = valores
    return df

def eliminar_columnas(df, columnas):
    """Elimina columnas específicas del DataFrame"""
    return df.drop(columns=columnas)

def ordenar_por_columna(df, columna, ascendente=True):
    """Ordena el DataFrame por una columna"""
    return df.sort_values(by=columna, ascending=ascendente)

def agrupar_y_promediar(df, columna_grupo, columna_valor):
    """Agrupa por una columna y calcula el promedio de otra columna"""
    return df.groupby(columna_grupo)[columna_valor].mean()

if __name__ == "__main__":
    data = {
        'Nombre': ['Ana', 'Luis', 'Carla', 'Juan'],
        'Edad': [23, 35, 29, 41],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
    }
    df = pd.DataFrame(data)

    print("Agregar columna Salario:")
    print(agregar_columna(df, 'Salario', [2000, 3000, 2500, 4000]))

    print("\nEliminar columna Edad:")
    print(eliminar_columnas(df, ['Edad']))

    print("\nOrdenar por Edad descendente:")
    print(ordenar_por_columna(df, 'Edad', ascendente=False))

    print("\nPromedio de Edad por Ciudad:")
    print(agrupar_y_promediar(df, 'Ciudad', 'Edad'))
