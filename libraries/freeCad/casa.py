import FreeCAD as App
import Part

doc = App.newDocument("Casa_Objetos_Separados")

# =====================
# PARAMETROS GENERALES
# =====================
ANCHO = 8000
LARGO = 12000
ALTO = 2700

MURO_EXT = 200
MURO_INT = 120

PUERTA_W = 900
PUERTA_H = 2100

VENTANA_W = 1200
VENTANA_H = 1200
VENTANA_Z = 900

# =====================
# FUNCION MURO
# =====================
def muro(nombre, x, y, z, w, d, h):
    obj = doc.addObject("Part::Feature", nombre)
    obj.Shape = Part.makeBox(w, d, h, App.Vector(x, y, z))
    return obj

# =====================
# MUROS EXTERIORES
# =====================
muro("Muro_Frontal",     0, 0, 0, ANCHO, MURO_EXT, ALTO)
muro("Muro_Fondo",       0, LARGO - MURO_EXT, 0, ANCHO, MURO_EXT, ALTO)
muro("Muro_Izquierdo",   0, 0, 0, MURO_EXT, LARGO, ALTO)
muro("Muro_Derecho",     ANCHO - MURO_EXT, 0, 0, MURO_EXT, LARGO, ALTO)

# =====================
# PASILLO CENTRAL
# =====================
PASILLO_X = ANCHO / 2 - MURO_INT / 2
muro("Muro_Pasillo", PASILLO_X, 2000, 0, MURO_INT, 8000, ALTO)

# =====================
# DORMITORIOS (3)
# =====================
# Separaciones horizontales
muro("Sep_Dorm_1", MURO_EXT, 4000, 0, ANCHO/2 - MURO_EXT, MURO_INT, ALTO)
muro("Sep_Dorm_2", MURO_EXT, 7000, 0, ANCHO/2 - MURO_EXT, MURO_INT, ALTO)

# =====================
# BAÑO
# =====================
muro("Muro_Bano", ANCHO/2 + MURO_INT/2, 6000, 0, ANCHO/2 - MURO_EXT, MURO_INT, ALTO)

# =====================
# PUERTA PRINCIPAL
# =====================
puerta = doc.addObject("Part::Feature", "Puerta_Principal")
puerta.Shape = Part.makeBox(
    PUERTA_W,
    MURO_EXT,
    PUERTA_H,
    App.Vector(ANCHO/2 - PUERTA_W/2, 0, 0)
)

# =====================
# VENTANAS
# =====================
def ventana(nombre, x, y, z, w, d, h):
    obj = doc.addObject("Part::Feature", nombre)
    obj.Shape = Part.makeBox(w, d, h, App.Vector(x, y, z))
    return obj

# Living
ventana("Ventana_Living", 1000, 0, VENTANA_Z, VENTANA_W, MURO_EXT, VENTANA_H)

# Dormitorios
ventana("Ventana_Dorm_1", 0, 3000, VENTANA_Z, MURO_EXT, VENTANA_W, VENTANA_H)
ventana("Ventana_Dorm_2", 0, 6000, VENTANA_Z, MURO_EXT, VENTANA_W, VENTANA_H)
ventana("Ventana_Dorm_3", 0, 9000, VENTANA_Z, MURO_EXT, VENTANA_W, VENTANA_H)

doc.recompute()
