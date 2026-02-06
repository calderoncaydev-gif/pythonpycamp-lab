"""
18_exceptions.py
----------------
Manejo de errores y excepciones en Python.
"""

try:
    x = int(input("Ingrese un número: "))
    result = 10 / x
except ValueError:
    print("Error: Debe ingresar un número válido")
except ZeroDivisionError:
    print("Error: División por cero no permitida")
except Exception as e:
    print(f"Error inesperado: {e}")
else:
    print(f"Resultado: {result}")
finally:
    print("Fin del bloque try/except")

# Lanzar excepciones
def check_positive(n):
    if n < 0:
        raise ValueError("El número debe ser positivo")
    return n

print(check_positive(5))
# print(check_positive(-1))  # Lanza ValueError
