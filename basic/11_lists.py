"""
11_lists.py
-----------
Listas en Python.
"""

# Crear listas
numbers = [1, 2, 3, 4, 5]
names = ["Ana", "Luis", "Pedro"]

# Acceso
print(numbers[0])
print(numbers[-1])

# Modificar
numbers[0] = 10

# Métodos comunes
numbers.append(6)
numbers.extend([7, 8])
numbers.insert(1, 20)
numbers.remove(3)
last = numbers.pop()

print(numbers)
print(last)

# Recorrer lista
for n in numbers:
    print(n)

# Ordenar
numbers.sort()
numbers.sort(reverse=True)

# Longitud
print(len(numbers))
