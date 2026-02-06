"""
07_functions.py
---------------
Funciones en Python.
"""

# Definición básica
def greet(name):
    return f"Hola {name}"

print(greet("Juan"))

# Parámetros con valor por defecto
def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(3, 3))

# Múltiples valores de retorno
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    return sum_, diff

result_sum, result_diff = calculate(10, 5)
print(result_sum, result_diff)

# Función lambda
square = lambda x: x ** 2
print(square(4))
