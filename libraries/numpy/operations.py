"""
operations.py
Funciones que combinan arrays.
"""

import numpy as np

def sumar(a, b):
    return np.add(a, b)

def multiplicar(a, b):
    return np.multiply(a, b)

def producto_punto(a, b):
    return np.dot(a, b)

def transponer(a):
    return a.T

if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print("a:", a)
    print("b:", b)
    print("Suma:", sumar(a, b))
    print("Multiplicación:", multiplicar(a, b))
    print("Producto punto:", producto_punto(a, b))
    print("Transpuesta de a reshaped:\n", transponer(a.reshape(3,1)))
