"""
arrays.py
Funciones para crear y mostrar arrays de NumPy.
"""

import numpy as np

def ejemplos_creacion():
    """Crear diferentes tipos de arrays de NumPy."""
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.arange(10)          # 0,1,...,9
    arr3 = np.linspace(0, 1, 5)   # 5 valores entre 0 y 1
    arr4 = np.zeros((2, 3))       # array 2x3 de ceros
    arr5 = np.ones((3, 2))        # array 3x2 de unos

    return arr1, arr2, arr3, arr4, arr5

if __name__ == "__main__":
    a1, a2, a3, a4, a5 = ejemplos_creacion()
    print("1D array:", a1)
    print("arange:", a2)
    print("linspace:", a3)
    print("zeros:\n", a4)
    print("ones:\n", a5)
