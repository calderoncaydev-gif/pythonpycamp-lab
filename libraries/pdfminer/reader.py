"""
reader.py
Funciones para leer texto desde PDFs usando PDFMiner
"""

from pdfminer.high_level import extract_text

def extraer_texto(ruta_pdf):
    texto = extract_text(ruta_pdf)

    if not texto or texto.strip() == "":
        raise ValueError("El PDF no contiene texto extraíble")

    return texto
