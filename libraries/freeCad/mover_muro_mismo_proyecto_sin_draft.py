import FreeCAD as App

doc = App.ActiveDocument
muro = doc.getObject("Wall")

# Obtener posición actual
pos_actual = muro.Placement.Base

# Crear nueva posición sumando desplazamiento
nueva_pos = pos_actual + App.Vector(0, 1000, 0)

# Asignar nueva posición
muro.Placement.Base = nueva_pos

doc.recompute()

print("✅ Muro movido 1000 mm en eje Y")
