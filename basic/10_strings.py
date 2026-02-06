"""
10_strings.py
-------------
Strings en Python.
"""

text = "Hola Mundo"
name = "Ana"

# Indexado y slicing
print(text[0])      # H
print(text[-1])     # o
print(text[0:4])    # Hola

# Métodos útiles
print(text.lower())
print(text.upper())
print(text.replace("Mundo", "Python"))
print(text.split())   # ['Hola', 'Mundo']

# Formateo
age = 25
print(f"{name} tiene {age} años")
print("{} tiene {} años".format(name, age))

# Strings multilínea
multi = """Línea 1
Línea 2
Línea 3"""
print(multi)
