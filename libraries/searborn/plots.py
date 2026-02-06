"""
plots.py
Funciones para generar gráficos usando Seaborn.
"""

import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograma(df, columna, bins=10, titulo="Histograma", estilo='darkgrid'):
    """
    Crea un histograma de una columna del DataFrame.
    """
    sns.set_style(estilo)
    plt.figure(figsize=(8,5))
    sns.histplot(df[columna], bins=bins, kde=True, color='skyblue')
    plt.title(titulo)
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.show()

def plot_box(df, columna, titulo="Boxplot", estilo='whitegrid'):
    """
    Crea un boxplot de una columna del DataFrame.
    """
    sns.set_style(estilo)
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[columna], color='lightgreen')
    plt.title(titulo)
    plt.show()

def plot_scatter(df, x_col, y_col, hue_col=None, titulo="Scatterplot", estilo='darkgrid'):
    """
    Crea un scatterplot de dos columnas del DataFrame.
    """
    sns.set_style(estilo)
    plt.figure(figsize=(8,5))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue_col, palette="Set2")
    plt.title(titulo)
    plt.show()
