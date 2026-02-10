import FreeCAD as App
import Part

doc = App.newDocument("Tubo_PVC_110_Hidroponia")

# =========================
# PARÁMETROS DEL TUBO
# =========================
largo = 1000                 # 100 cm
diam_ext = 110
espesor = 5
radio_ext = diam_ext / 2
radio_int = (diam_ext - 2 * espesor) / 2

# =========================
# CREAR TUBO HUECO
# =========================
tubo_exterior = Part.makeCylinder(
    radio_ext,
    largo,
    App.Vector(0, 0, 0),
    App.Vector(1, 0, 0)
)

tubo_interior = Part.makeCylinder(
    radio_int,
    largo + 2,
    App.Vector(-1, 0, 0),
    App.Vector(1, 0, 0)
)

tubo = tubo_exterior.cut(tubo_interior)

# =========================
# AGUJEROS
# =========================
diam_agujero = 50
radio_agujero = diam_agujero / 2
separacion = 200
profundidad = 150

agujeros = []
x = 100

while x <= largo - 100:
    agujero = Part.makeCylinder(
        radio_agujero,
        profundidad,
        App.Vector(x, radio_ext, radio_ext),
        App.Vector(0, -1, 0)
    )
    agujeros.append(agujero)
    x += separacion

# Unir agujeros
agujeros_union = agujeros[0]
for a in agujeros[1:]:
    agujeros_union = agujeros_union.fuse(a)

# Cortar el tubo
tubo_final = tubo.cut(agujeros_union)

# =========================
# MOSTRAR EN FREECAD
# =========================
obj = doc.addObject("Part::Feature", "Tubo_PVC_110mm")
obj.Shape = tubo_final
obj.ViewObject.ShapeColor = (0.9, 0.9, 0.9)

doc.recompute()

print("✅ Tubo PVC 110 mm con agujeros creado correctamente")
