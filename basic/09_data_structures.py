"""
09_data_structures.py
---------------------
Resumen rápido de estructuras de datos básicas.
"""

# Lista
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# Tupla (inmutable)
coordinates = (10, 20)
print(coordinates)

# Set (sin duplicados)
numbers = {1, 2, 3, 3, 2}
print(numbers)

# Diccionario
person = {"name": "Ana", "age": 25}
print(person)

# Convertir entre estructuras
fruits_set = set(fruits)
fruits_list = list(fruits_set)
print(fruits_set, fruits_list)
