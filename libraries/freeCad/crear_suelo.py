import FreeCAD
import Part

doc = FreeCAD.newDocument("Terreno")

# Dimensiones en mm 1 hectarea
# largo = 100000   # 100 m
# ancho = 100000   # 100 m
# espesor = 200    # 0.20 m


# Dimensiones en mm (CASA)
largo   = 10000   # 10 m
ancho   = 8000    # 8 m
espesor = 200     # 0.20 m (muros)

# Crear el sólido
suelo = Part.makeBox(largo, ancho, espesor)

# Agregar al documento
obj = doc.addObject("Part::Feature", "Suelo")
obj.Shape = suelo

# Recalcular
doc.recompute()
