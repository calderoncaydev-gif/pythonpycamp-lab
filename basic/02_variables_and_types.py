"""
02_variables_and_types.py
-------------------------
Repaso de variables y tipos de datos en Python.
"""

# Variables
name = "Juan"
age = 30
height = 1.75
is_active = True

# Python es de tipado dinámico
age = 31  # cambia el valor sin problema

# Tipos básicos
print(type(name))       # str
print(type(age))        # int
print(type(height))     # float
print(type(is_active))  # bool

# Asignación múltiple
x, y, z = 1, 2, 3
print(x, y, z)

# Convención de nombres (snake_case)
user_name = "admin"
total_score = 100

# Conversión de tipos (casting)
age_str = str(age)
height_int = int(height)

print(age_str, type(age_str))
print(height_int, type(height_int))

# Constantes (por convención, no por el lenguaje)
PI = 3.1416
MAX_USERS = 1000

"""
Notas rápidas:
- No se declaran tipos explícitamente
- type() ayuda para debugging
- Las constantes se escriben en MAYÚSCULAS por convención
"""
