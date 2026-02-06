"""
images.py
Funciones para cargar y mostrar imágenes usando OpenCV.
"""

import cv2

def cargar_imagen(ruta, color=True):
    """
    Carga una imagen desde disco.
    color=True -> BGR
    color=False -> escala de grises
    """
    flag = cv2.IMREAD_COLOR if color else cv2.IMREAD_GRAYSCALE
    img = cv2.imread(ruta, flag)
    if img is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {ruta}")
    return img

def mostrar_imagen(img, titulo="Imagen"):
    """
    Muestra la imagen en una ventana.
    """
    cv2.imshow(titulo, img)
    cv2.waitKey(0)  # Espera a que se presione cualquier tecla
    cv2.destroyAllWindows()
