"""
23_best_practices.py
--------------------
Buenas prácticas de Python.
"""

# Nombres claros (snake_case)
user_name = "Ana"

# Evitar código duplicado
def greet(name):
    return f"Hola {name}"

print(greet("Juan"))
print(greet("Ana"))

# Comentarios y docstrings
def multiply(a, b):
    """
    Multiplica dos números y devuelve el resultado
    """
    return a * b

# Modularidad: dividir en archivos y funciones
# Organización: basics/ -> fundamentals, libraries/ -> librerías, projects/ -> proyectos

# Leer documentación y PEP8
# https://www.python.org/dev/peps/pep-0008/

# Manejo de errores y pruebas siempre
try:
    print(multiply(2, "3"))  # Evitar errores inesperados
except TypeError:
    print("Tipo de dato incorrecto")
