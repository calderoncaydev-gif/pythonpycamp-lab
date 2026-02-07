"""
basic.py
Creación y manipulación básica de grafos con NetworkX
"""

import networkx as nx

def crear_grafo_simple():
    G = nx.Graph()

    G.add_node("Ana")
    G.add_node("Luis")
    G.add_edge("Ana", "Luis")
    G.add_edge("Luis", "Carla")
    G.add_edge("Ana", "Carla")

    return G

def info_grafo(G):
    return {
        "nodos": list(G.nodes),
        "aristas": list(G.edges),
        "num_nodos": G.number_of_nodes(),
        "num_aristas": G.number_of_edges()
    }
