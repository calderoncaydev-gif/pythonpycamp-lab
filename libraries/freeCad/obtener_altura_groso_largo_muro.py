import FreeCAD as App

doc = App.ActiveDocument
muro = doc.getObject("Wall")

# ===============================
# ALTURA
# ===============================
altura = muro.Height

# ===============================
# GROSOR
# ===============================
grosor = muro.Width

# ===============================
# LARGO (desde la línea base)
# ===============================
linea = muro.Base
largo = (linea.End - linea.Start).Length

print("Altura:", altura, "mm")
print("Grosor:", grosor, "mm")
print("Largo:", largo, "mm")
