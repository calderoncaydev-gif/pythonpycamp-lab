"""
16_modules_and_packages.py
--------------------------
Uso de módulos y paquetes en Python.
"""

# Importar módulo estándar
import math
print(math.sqrt(16))
print(math.pi)

# Importar parte específica
from math import pow
print(pow(2, 3))

# Alias
import math as m
print(m.ceil(2.3))

# Crear módulo propio (archivo my_module.py)
# import my_module
# my_module.my_function()

# Paquetes
# Estructura:
# my_package/
# ├── __init__.py
# └── submodule.py
# from my_package import submodule
