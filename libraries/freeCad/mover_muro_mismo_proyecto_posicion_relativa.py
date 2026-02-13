import FreeCAD as App
import Draft

doc = App.ActiveDocument

muro = doc.getObject("Wall")

# Mover 500 mm en X
# MOver 1000 mm en y
Draft.move(muro, App.Vector(500, 1000, 0))

doc.recompute()

print("✅ Muro movido 500 mm en eje X")
