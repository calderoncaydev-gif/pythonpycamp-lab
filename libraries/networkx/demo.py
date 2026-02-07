"""
demo.py
Ejemplo completo usando NetworkX
"""

from basic import crear_grafo_simple, info_grafo
from metrics import grado_nodos, centralidad, camino_mas_corto
from visualization import dibujar_grafo

def main():
    G = crear_grafo_simple()

    print("INFO DEL GRAFO")
    print(info_grafo(G))

    print("\nGRADO DE NODOS")
    print(grado_nodos(G))

    print("\nCENTRALIDAD")
    print(centralidad(G))

    print("\nCAMINO MÁS CORTO Ana -> Carla")
    print(camino_mas_corto(G, "Ana", "Carla"))

    dibujar_grafo(G, "Red de Personas")

if __name__ == "__main__":
    main()
