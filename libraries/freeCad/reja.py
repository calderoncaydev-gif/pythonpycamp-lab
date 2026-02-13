import FreeCAD as App
import Part

doc = App.newDocument("Reja_Metalica")

# ======================
# PARAMETROS (mm)
# ======================
ancho = 1200
alto = 1800
perfil_marco = 40
perfil_barra = 20
separacion = 120
espesor = 20

# ======================
# MARCO
# ======================
marco_exterior = Part.makeBox(ancho, perfil_marco, alto)
marco_interior = Part.makeBox(
    ancho - 2 * perfil_marco,
    perfil_marco,
    alto - 2 * perfil_marco,
    App.Vector(perfil_marco, 0, perfil_marco)
)

marco = marco_exterior.cut(marco_interior)

obj_marco = doc.addObject("Part::Feature", "Marco")
obj_marco.Shape = marco

# ======================
# BARRAS VERTICALES
# ======================
x = perfil_marco + separacion
barras = []

while x < ancho - perfil_marco:
    barra = Part.makeBox(
        perfil_barra,
        espesor,
        alto - 2 * perfil_marco,
        App.Vector(x, 0, perfil_marco)
    )
    barras.append(barra)
    x += separacion

# ======================
# UNION
# ======================
reja = marco
for b in barras:
    reja = reja.fuse(b)

obj_reja = doc.addObject("Part::Feature", "Reja_Completa")
obj_reja.Shape = reja

doc.recompute()
