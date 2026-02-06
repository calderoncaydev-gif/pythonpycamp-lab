"""
22_testing_basics.py
-------------------
Pruebas básicas en Python.
"""

# Función a testear
def add(a, b):
    return a + b

# Tests simples
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

test_add()
print("Todos los tests pasaron ✅")

# pytest o unittest son recomendables para proyectos grandes
