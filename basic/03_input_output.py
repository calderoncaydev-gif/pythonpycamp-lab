"""
03_input_output.py
------------------
Entrada y salida de datos.
"""

# Entrada de datos (input siempre devuelve string)
name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))

# Salida de datos
print("Nombre:", name)
print("Edad:", age)

# f-strings (recomendado)
print(f"Hola {name}, tienes {age} años")
