"""
20_standard_library_intro.py
----------------------------
Introducción a la biblioteca estándar de Python.
"""

import os
import sys
import datetime
import random

# OS
print("Directorio actual:", os.getcwd())

# Sys
print("Versión de Python:", sys.version)

# DateTime
now = datetime.datetime.now()
print("Fecha y hora actuales:", now)

# Random
print("Número aleatorio:", random.randint(1, 10))
