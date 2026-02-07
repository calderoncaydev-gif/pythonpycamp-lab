"""
visualization.py
Funciones para visualizar grafos
"""

import matplotlib.pyplot as plt
import networkx as nx

def dibujar_grafo(G, titulo="Grafo"):
    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=1500,
        edge_color="gray",
        font_size=10
    )

    plt.title(titulo)
    plt.show()
