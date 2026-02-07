"""
demo.py
Ejemplo completo con PDFMiner
"""

from reader import extraer_texto
from metadata import obtener_metadata
from utils import limpiar_texto

def main():
    ruta_pdf = "libraries/pdfminer/samples/example.pdf"

    print("📄 LEYENDO PDF...\n")

    texto = extraer_texto(ruta_pdf)
    texto_limpio = limpiar_texto(texto)

    print("=== TEXTO EXTRAÍDO (primeros 500 caracteres) ===")
    print(texto_limpio[:500])

    print("\n=== METADATOS ===")
    metadata = obtener_metadata(ruta_pdf)
    for k, v in metadata.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
