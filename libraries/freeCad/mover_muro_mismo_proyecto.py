"""
Modificar propiedades de un muro existente en FreeCAD (Arch/BIM)

Se modificará:
- Altura (Height)
- Grosor (Width)
- Anchor (alineación respecto a la línea base)
"""

import FreeCAD as App

doc = App.ActiveDocument

# Obtener el muro por nombre
muro = doc.getObject("Wall")

# ==========================================================
# 1️⃣ MODIFICAR ALTURA (en milímetros)
# ==========================================================
muro.Height = 3000   # Nueva altura = 3000 mm (3 metros)

# ==========================================================
# 2️⃣ MODIFICAR GROSOR (Width)
# ==========================================================
muro.Width = 250     # Nuevo espesor = 250 mm

# ==========================================================
# 3️⃣ MODIFICAR ANCHOR (alineación del muro)
# ==========================================================
"""
Anchor define cómo se posiciona el muro respecto a su línea base.

Valores posibles:
0 = Centro
1 = Izquierda
2 = Derecha
"""

muro.Align = "center"     # Opciones: "Left", "Right", "Center"

# Actualizar documento
doc.recompute()

print("✅ Muro modificado correctamente")
