"""
demo.py
Demostración de funciones de OpenCV.
"""

from images import cargar_imagen, mostrar_imagen
from processing import convertir_grises, aplicar_blur, detectar_bordes

# Cargar imagen
img = cargar_imagen(r"C:\Users\56934\Documents\python\pytonpycamp-lab\libraries\opencv\2.png")
  # <- reemplaza con tu imagen

# Mostrar imagen original
mostrar_imagen(img, "Original")

# Convertir a escala de grises
gris = convertir_grises(img)
mostrar_imagen(gris, "Escala de Grises")

# Aplicar blur
blur = aplicar_blur(gris, ksize=7)
mostrar_imagen(blur, "Blur Gaussiano")

# Detectar bordes
bordes = detectar_bordes(blur)
mostrar_imagen(bordes, "Bordes Canny")
