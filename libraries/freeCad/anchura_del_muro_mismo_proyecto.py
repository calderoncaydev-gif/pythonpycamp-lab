import FreeCAD as App

doc = App.ActiveDocument

# Obtener el muro
muro = doc.getObject("Wall")

# Obtener la línea base del muro
linea = muro.Base

# Punto inicial (no lo cambiamos)
inicio = linea.Start

# Punto final actual
fin_actual = linea.End

# Aumentar 1000 mm en X
nuevo_fin = App.Vector(fin_actual.x + 500, fin_actual.y, fin_actual.z)

# Asignar nuevo punto final
linea.End = nuevo_fin

doc.recompute()

print("✅ Muro extendido 1000 mm en eje X")
