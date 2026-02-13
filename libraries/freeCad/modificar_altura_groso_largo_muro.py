import FreeCAD as App

doc = App.ActiveDocument
muro = doc.getObject("Wall")

# ===================================
# MODIFICAR ALTURA
# ===================================
muro.Height = 2800   # 2800 mm

# ===================================
# MODIFICAR GROSOR
# ===================================
muro.Width = 250     # 250 mm

# ===================================
# MODIFICAR LARGO (Length)
# ===================================
nuevo_largo = 30000   # 6000 mm total

linea = muro.Base

linea.End = App.Vector(
    linea.Start.x + nuevo_largo,
    linea.Start.y,
    linea.Start.z
)

doc.recompute()

print("✅ Dimensiones modificadas correctamente")
