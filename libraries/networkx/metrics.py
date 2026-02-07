"""
metrics.py
Métricas comunes en grafos
"""

import networkx as nx

def grado_nodos(G):
    return dict(G.degree())

def centralidad(G):
    return nx.degree_centrality(G)

def camino_mas_corto(G, origen, destino):
    return nx.shortest_path(G, origen, destino)
