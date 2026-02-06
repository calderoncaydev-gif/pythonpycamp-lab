"""
test_styles.py
Ejemplo de uso de styles.py para ver cómo se aplican los estilos a gráficos Matplotlib.
"""

import matplotlib.pyplot as plt
from styles import estilo_dark, estilo_light, configurar_titulo, configurar_ejes, activar_grilla, aplicar_limites

# ======= Selecciona estilo =======
# Para probar, cambia entre estilo_dark() o estilo_light()
estilo_dark()
# estilo_light()

# ======= Crear datos de ejemplo =======
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 20]

# ======= Crear figura y eje =======
fig, ax = plt.subplots()

# ======= Graficar línea =======
ax.plot(x, y, marker='o', linestyle='-', color='cyan', label='Ejemplo')

# ======= Aplicar funciones de styles.py =======
configurar_titulo(ax, "Gráfico de ejemplo", fontsize=18)
configurar_ejes(ax, "Eje X", "Eje Y", fontsize=14)
activar_grilla(ax, estilo='--', color='white', alpha=0.7)
aplicar_limites(ax, xlim=(0,6), ylim=(0,25))

# ======= Mostrar leyenda =======
ax.legend()

# ======= Mostrar gráfico =======
plt.show()
