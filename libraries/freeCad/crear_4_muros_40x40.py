"""
Script FreeCAD BIM / Arch
Crea 4 muros formando un rectángulo de 40 x 40 metros.

Todas las unidades en milímetros (mm).
Puedes modificar:
- Largo X
- Largo Y
- Altura
- Grosor
"""

import FreeCAD as App
import Draft
import Arch

# ==========================================================
# 1️⃣ Crear documento nuevo si no existe
# ==========================================================
doc = App.ActiveDocument
if doc is None:
    doc = App.newDocument("Proyecto_40x40")

# ==========================================================
# 2️⃣ PARÁMETROS MODIFICABLES
# ==========================================================

largo_x = 40000      # 40 metros en X (40000 mm)
largo_y = 40000      # 40 metros en Y (40000 mm)
altura = 3000        # Altura del muro (3000 mm = 3m)
grosor = 300         # Espesor del muro (300 mm)

# ==========================================================
# 3️⃣ Crear líneas base del rectángulo
# ==========================================================

# Punto de inicio
p1 = App.Vector(0, 0, 0)
p2 = App.Vector(largo_x, 0, 0)
p3 = App.Vector(largo_x, largo_y, 0)
p4 = App.Vector(0, largo_y, 0)

# Crear líneas
linea1 = Draft.makeLine(p1, p2)  # Muro inferior (X)
linea2 = Draft.makeLine(p2, p3)  # Muro derecho (Y)
linea3 = Draft.makeLine(p3, p4)  # Muro superior (-X)
linea4 = Draft.makeLine(p4, p1)  # Muro izquierdo (-Y)

doc.recompute()

# ==========================================================
# 4️⃣ Crear muros a partir de líneas
# ==========================================================

muros = []

for linea in [linea1, linea2, linea3, linea4]:
    muro = Arch.makeWall(linea)
    muro.Height = altura
    muro.Width = grosor
    muros.append(muro)

doc.recompute()

print("✅ 4 Muros creados correctamente (40x40 metros)")
