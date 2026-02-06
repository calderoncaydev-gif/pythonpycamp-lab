"""
08_scope.py
-----------
Alcance de variables en Python: local, global y nonlocal.
"""

# Variable global
x = 10

def local_scope():
    # Variable local
    x = 5
    print("Dentro de la función:", x)

local_scope()
print("Fuera de la función:", x)  # sigue siendo 10

# Usando global
def modify_global():
    global x
    x = 20

modify_global()
print("Después de modificar global:", x)

# Nonlocal (para closures / funciones anidadas)
def outer():
    y = 1
    def inner():
        nonlocal y
        y += 5
        print("Inner:", y)
    inner()
    print("Outer:", y)

outer()
