"""
metadata.py
Extracción de metadatos de PDFs
"""

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

def obtener_metadata(ruta_pdf):
    with open(ruta_pdf, "rb") as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)

        if not doc.info:
            return {}

        return doc.info[0]
