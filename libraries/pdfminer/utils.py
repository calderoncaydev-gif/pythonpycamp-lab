"""
utils.py
Funciones auxiliares para limpiar texto
"""

import re

def limpiar_texto(texto):
    texto = texto.replace("\n", " ")
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()
