"""
Crear muro orientado en eje Y en FreeCAD (Arch/BIM)
Todas las unidades en milímetros
"""

import FreeCAD as App
import Draft
import Arch

# ==================================================
# 1️⃣ Crear documento (si no existe uno)
# ==================================================
doc = App.ActiveDocument
if doc is None:
    doc = App.newDocument("Proyecto_Muro_Y")

# ==================================================
# 2️⃣ Definir dimensiones
# ==================================================
largo_muro = 4000    # 4000 mm en eje Y
altura_muro = 2500   # 2500 mm altura
espesor_muro = 200   # 200 mm grosor

# ==================================================
# 3️⃣ Crear línea base en eje Y
# ==================================================
linea_base = Draft.makeLine(
    App.Vector(10000, 10000, 0),               # Punto inicial
    App.Vector(0, largo_muro, 0)      # Punto final en Y
)

doc.recompute()

# ==================================================
# 4️⃣ Crear muro
# ==================================================
muro_y = Arch.makeWall(linea_base)

muro_y.Height = altura_muro
muro_y.Width = espesor_muro

doc.recompute()

print("✅ Muro creado en eje Y correctamente")
