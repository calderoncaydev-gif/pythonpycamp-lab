"""
demo.py
Demostración de gráficos con Seaborn.
"""

import pandas as pd
from plots import plot_histograma, plot_box, plot_scatter

# Crear un DataFrame de ejemplo
data = {
    'Edad': [23, 35, 29, 41, 30, 26, 38, 42],
    'Ingreso': [2000, 4000, 3200, 5000, 3500, 2800, 4200, 4800],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Madrid', 'Sevilla', 'Barcelona', 'Valencia']
}

df = pd.DataFrame(data)

# Histograma
plot_histograma(df, 'Edad', bins=5, titulo="Distribución de Edad")

# Boxplot
plot_box(df, 'Ingreso', titulo="Boxplot de Ingresos")

# Scatterplot
plot_scatter(df, 'Edad', 'Ingreso', hue_col='Ciudad', titulo="Edad vs Ingreso por Ciudad")
