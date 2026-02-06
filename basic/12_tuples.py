"""
12_tuples.py
------------
Tuplas en Python (inmutables).
"""

# Crear tuplas
coords = (10, 20)
names = ("Ana", "Luis", "Pedro")

# Acceso
print(coords[0])
print(names[-1])

# Unpacking
x, y = coords
print(x, y)

# Métodos limitados
print(len(names))
print(names.count("Ana"))
print(names.index("Pedro"))
