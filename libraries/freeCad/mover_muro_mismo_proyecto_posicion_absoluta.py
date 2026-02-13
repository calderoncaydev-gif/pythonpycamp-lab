import FreeCAD as App

doc = App.ActiveDocument

# Obtener el muro por nombre (por seguridad)
muro = doc.getObject("Wall")

# Mover el muro a una nueva posición absoluta
# X = 1000 mm 
# Y = 2000 mm
# Z = 0 mm
muro.Placement.Base = App.Vector(0, 0, 0)

doc.recompute()

print("✅ Muro movido a posición absoluta (1000,2000,0)")
