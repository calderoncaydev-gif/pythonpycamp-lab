"""
styles.py
Funciones para aplicar estilos y personalizar gráficos Matplotlib.
No ejecuta nada por sí mismo, solo sirve como módulo.
"""

import matplotlib.pyplot as plt

# =========================
# Estilos predefinidos
# =========================
def estilo_dark():
    """
    Aplica un estilo oscuro a los gráficos.
    """
    plt.style.use('dark_background')
    plt.rcParams.update({
        'axes.facecolor': '#222222',
        'axes.edgecolor': 'white',
        'axes.labelcolor': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white',
        'figure.facecolor': '#222222',
        'grid.color': 'gray',
        'grid.linestyle': '--',
        'grid.alpha': 0.5,
        'font.size': 12
    })


def estilo_light():
    """
    Aplica un estilo claro y limpio a los gráficos.
    """
    plt.style.use('default')
    plt.rcParams.update({
        'axes.facecolor': 'white',
        'axes.edgecolor': 'black',
        'axes.labelcolor': 'black',
        'xtick.color': 'black',
        'ytick.color': 'black',
        'figure.facecolor': 'white',
        'grid.color': 'gray',
        'grid.linestyle': '--',
        'grid.alpha': 0.5,
        'font.size': 12
    })

# =========================
# Funciones para configurar gráficos
# =========================
def configurar_titulo(ax, titulo, fontsize=16, bold=True, color='black'):
    """
    Configura el título de un gráfico.
    """
    weight = 'bold' if bold else 'normal'
    ax.set_title(titulo, fontsize=fontsize, fontweight=weight, color=color)

def configurar_ejes(ax, xlabel="", ylabel="", fontsize=12, color='black'):
    """
    Configura etiquetas de los ejes.
    """
    ax.set_xlabel(xlabel, fontsize=fontsize, color=color)
    ax.set_ylabel(ylabel, fontsize=fontsize, color=color)

def activar_grilla(ax, estilo='--', color='gray', alpha=0.5):
    """
    Activa la grilla en un gráfico.
    """
    ax.grid(True, linestyle=estilo, color=color, alpha=alpha)

def aplicar_limites(ax, xlim=None, ylim=None):
    """
    Aplica límites a los ejes si se especifica.
    """
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)
