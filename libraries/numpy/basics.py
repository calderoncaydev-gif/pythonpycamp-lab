"""
basic.py
Operaciones simples sobre arrays de NumPy.
"""

import numpy as np

def suma_total(arr):
    return np.sum(arr)

def promedio(arr):
    return np.mean(arr)

def maximo(arr):
    return np.max(arr)

def minimo(arr):
    return np.min(arr)

if __name__ == "__main__":
    arr = np.array([10, 20, 30, 40])
    print("Array:", arr)
    print("Suma:", suma_total(arr))
    print("Promedio:", promedio(arr))
    print("Máximo:", maximo(arr))
    print("Mínimo:", minimo(arr))
