import FreeCAD as App
import Part

doc = App.newDocument("Escalera_Fierro")

# =========================
# MEDIDAS GENERALES
# =========================
altura_total = 2800
largo_total = 3500
ancho = 900

peldaños = 5
altura_peldaño = altura_total / peldaños
huella = largo_total / peldaños

# Perfiles
larguero_h = 100
larguero_w = 50

peldaño_h = 50
peldaño_w = 30

# =========================
# LARGUEROS LATERALES
# =========================
larguero_izq = Part.makeBox(
    largo_total,
    larguero_w,
    larguero_h,
    App.Vector(0, 0, 0)
)

larguero_der = Part.makeBox(
    largo_total,
    larguero_w,
    larguero_h,
    App.Vector(0, ancho - larguero_w, 0)
)

largueros = larguero_izq.fuse(larguero_der)

# =========================
# PELDAÑOS
# =========================
peldaños_lista = []

for i in range(peldaños):
    x = i * huella
    z = i * altura_peldaño

    peldaño = Part.makeBox(
        huella,
        ancho,
        peldaño_h,
        App.Vector(x, 0, z)
    )
    peldaños_lista.append(peldaño)

peldaños_union = peldaños_lista[0]
for p in peldaños_lista[1:]:
    peldaños_union = peldaños_union.fuse(p)

# =========================
# UNIÓN FINAL
# =========================
escalera = largueros.fuse(peldaños_union)

obj = doc.addObject("Part::Feature", "Escalera_Fierro")
obj.Shape = escalera
obj.ViewObject.ShapeColor = (0.4, 0.4, 0.4)

doc.recompute()

print("✅ Escalera de fierro creada correctamente")
