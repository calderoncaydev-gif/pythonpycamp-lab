"""
processing.py
Funciones de procesamiento de imágenes con OpenCV.
"""

import cv2

def convertir_grises(img):
    """
    Convierte una imagen a escala de grises.
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def aplicar_blur(img, ksize=5):
    """
    Aplica un filtro Gaussiano para suavizar la imagen.
    """
    return cv2.GaussianBlur(img, (ksize, ksize), 0)

def detectar_bordes(img, umbral1=50, umbral2=150):
    """
    Aplica el detector de bordes de Canny.
    """
    return cv2.Canny(img, umbral1, umbral2)
