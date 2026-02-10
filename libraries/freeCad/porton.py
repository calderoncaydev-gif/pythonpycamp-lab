import FreeCAD as App
import Part

doc = App.newDocument("Porton_Fierro")

# =========================
# MEDIDAS GENERALES
# =========================
ancho = 3000
alto = 1800

# Perfiles
marco_x = 50
marco_y = 30

barrote = 20
separacion = 120

# =========================
# FUNCIÓN PERFIL RECTANGULAR
# =========================
def perfil_rectangular(x, y, z, lx, ly, lz):
    return Part.makeBox(lx, ly, lz, App.Vector(x, y, z))

# =========================
# MARCO DEL PORTÓN
# =========================
marco = []

# Inferior
marco.append(perfil_rectangular(0, 0, 0, ancho, marco_y, marco_x))
# Superior
marco.append(perfil_rectangular(0, 0, alto - marco_x, ancho, marco_y, marco_x))
# Izquierdo
marco.append(perfil_rectangular(0, 0, 0, marco_x, marco_y, alto))
# Derecho
marco.append(perfil_rectangular(ancho - marco_x, 0, 0, marco_x, marco_y, alto))

marco_union = marco[0]
for p in marco[1:]:
    marco_union = marco_union.fuse(p)

# =========================
# BARROTES VERTICALES
# =========================
barrotes = []
x = marco_x + separacion

while x < ancho - marco_x:
    barrote_obj = perfil_rectangular(
        x,
        0,
        marco_x,
        barrote,
        marco_y,
        alto - 2 * marco_x
    )
    barrotes.append(barrote_obj)
    x += separacion

barrotes_union = barrotes[0]
for b in barrotes[1:]:
    barrotes_union = barrotes_union.fuse(b)

# =========================
# UNIÓN FINAL
# =========================
porton = marco_union.fuse(barrotes_union)

obj = doc.addObject("Part::Feature", "Porton_Fierro")
obj.Shape = porton
obj.ViewObject.ShapeColor = (0.3, 0.3, 0.3)

doc.recompute()

print("✅ Portón de fierro creado correctamente")
