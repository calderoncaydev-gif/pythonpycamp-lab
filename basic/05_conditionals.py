"""
05_conditionals.py
------------------
Condicionales if / elif / else.
"""

age = int(input("Ingrese su edad: "))

if age >= 18:
    print("Mayor de edad")
elif age >= 13:
    print("Adolescente")
else:
    print("Menor de edad")

# Operador ternario
status = "Adulto" if age >= 18 else "Menor"
print(status)
