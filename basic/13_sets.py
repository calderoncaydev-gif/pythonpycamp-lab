"""
13_sets.py
-----------
Sets en Python (colecciones únicas).
"""

nums = {1, 2, 3, 3, 2}
print(nums)  # {1, 2, 3}

# Operaciones
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

# Métodos
a.add(10)
a.remove(2)
a.discard(100)  # no da error
print(a)
