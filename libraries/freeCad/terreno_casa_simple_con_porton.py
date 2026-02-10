"""
PROYECTO VIVIENDA SIMPLE - FREECAD
---------------------------------
Incluye:
- Terreno de 1 hectárea (100 x 100 m)
- Muro perimetral con portón
- Casa simple rectangular

Autor: Tú 😄
Uso: Ejecutar como Macro o desde Consola Python
"""

import FreeCAD
import Part

# ==================================================
# 1️⃣ DOCUMENTO
# ==================================================
doc = FreeCAD.ActiveDocument
if doc is None:
    doc = FreeCAD.newDocument("Proyecto_Vivienda")

# ==================================================
# 2️⃣ TERRENO (1 hectárea)
# ==================================================
# 100 m x 100 m x 0.20 m
TERRENO_LARGO = 100000
TERRENO_ANCHO = 100000
TERRENO_ESPESOR = 200

terreno = Part.makeBox(TERRENO_LARGO, TERRENO_ANCHO, TERRENO_ESPESOR)
obj_terreno = doc.addObject("Part::Feature", "Terreno")
obj_terreno.Shape = terreno
obj_terreno.Placement.Base = FreeCAD.Vector(0, 0, 0)

# ==================================================
# 3️⃣ MURO PERIMETRAL
# ==================================================
MURO_ALTO = 2200
MURO_ESPESOR = 200
ANCHO_PORTON = 4000

# Fondo
muro_fondo = Part.makeBox(TERRENO_LARGO, MURO_ESPESOR, MURO_ALTO)
obj_fondo = doc.addObject("Part::Feature", "Muro_Fondo")
obj_fondo.Shape = muro_fondo
obj_fondo.Placement.Base = FreeCAD.Vector(0, TERRENO_ANCHO - MURO_ESPESOR, TERRENO_ESPESOR)

# Izquierdo
muro_izq = Part.makeBox(MURO_ESPESOR, TERRENO_ANCHO, MURO_ALTO)
obj_izq = doc.addObject("Part::Feature", "Muro_Izquierdo")
obj_izq.Shape = muro_izq
obj_izq.Placement.Base = FreeCAD.Vector(0, 0, TERRENO_ESPESOR)

# Derecho
muro_der = Part.makeBox(MURO_ESPESOR, TERRENO_ANCHO, MURO_ALTO)
obj_der = doc.addObject("Part::Feature", "Muro_Derecho")
obj_der.Shape = muro_der
obj_der.Placement.Base = FreeCAD.Vector(
    TERRENO_LARGO - MURO_ESPESOR, 0, TERRENO_ESPESOR
)

# Frente con hueco de portón
lado = (TERRENO_LARGO - ANCHO_PORTON) / 2

muro_frente_izq = Part.makeBox(lado, MURO_ESPESOR, MURO_ALTO)
obj_fi = doc.addObject("Part::Feature", "Muro_Frente_Izq")
obj_fi.Shape = muro_frente_izq
obj_fi.Placement.Base = FreeCAD.Vector(0, 0, TERRENO_ESPESOR)

muro_frente_der = Part.makeBox(lado, MURO_ESPESOR, MURO_ALTO)
obj_fd = doc.addObject("Part::Feature", "Muro_Frente_Der")
obj_fd.Shape = muro_frente_der
obj_fd.Placement.Base = FreeCAD.Vector(
    lado + ANCHO_PORTON, 0, TERRENO_ESPESOR
)

# ==================================================
# 4️⃣ PORTÓN
# ==================================================
PORTON_ANCHO = 4000
PORTON_ALTO = 2200
PORTON_ESPESOR = 80

porton = Part.makeBox(PORTON_ANCHO, PORTON_ESPESOR, PORTON_ALTO)
obj_porton = doc.addObject("Part::Feature", "Porton")
obj_porton.Shape = porton
obj_porton.Placement.Base = FreeCAD.Vector(
    lado, 0, TERRENO_ESPESOR
)

# ==================================================
# 5️⃣ CASA SIMPLE
# ==================================================
CASA_LARGO = 10000
CASA_ANCHO = 8000
CASA_ALTO = 2600
CASA_ESPESOR = 200

# Posición dentro del terreno
CASA_X = 45000
CASA_Y = 45000

# Radier
radier = Part.makeBox(CASA_LARGO, CASA_ANCHO, 150)
obj_radier = doc.addObject("Part::Feature", "Casa_Radier")
obj_radier.Shape = radier
obj_radier.Placement.Base = FreeCAD.Vector(CASA_X, CASA_Y, TERRENO_ESPESOR)

# Muros
muro_casa_izq = Part.makeBox(CASA_ESPESOR, CASA_ANCHO, CASA_ALTO)
obj_ci = doc.addObject("Part::Feature", "Casa_Muro_Izq")
obj_ci.Shape = muro_casa_izq
obj_ci.Placement.Base = FreeCAD.Vector(
    CASA_X, CASA_Y, TERRENO_ESPESOR + 150
)

muro_casa_der = Part.makeBox(CASA_ESPESOR, CASA_ANCHO, CASA_ALTO)
obj_cd = doc.addObject("Part::Feature", "Casa_Muro_Der")
obj_cd.Shape = muro_casa_der
obj_cd.Placement.Base = FreeCAD.Vector(
    CASA_X + CASA_LARGO - CASA_ESPESOR,
    CASA_Y,
    TERRENO_ESPESOR + 150
)

muro_casa_fondo = Part.makeBox(CASA_LARGO, CASA_ESPESOR, CASA_ALTO)
obj_cf = doc.addObject("Part::Feature", "Casa_Muro_Fondo")
obj_cf.Shape = muro_casa_fondo
obj_cf.Placement.Base = FreeCAD.Vector(
    CASA_X,
    CASA_Y + CASA_ANCHO - CASA_ESPESOR,
    TERRENO_ESPESOR + 150
)

muro_casa_frente = Part.makeBox(CASA_LARGO, CASA_ESPESOR, CASA_ALTO)
obj_cfr = doc.addObject("Part::Feature", "Casa_Muro_Frente")
obj_cfr.Shape = muro_casa_frente
obj_cfr.Placement.Base = FreeCAD.Vector(
    CASA_X,
    CASA_Y,
    TERRENO_ESPESOR + 150
)

# ==================================================
# 6️⃣ FINALIZAR
# ==================================================
doc.recompute()
FreeCAD.Gui.activeDocument().activeView().viewIsometric()
FreeCAD.Gui.SendMsgToActiveView("ViewFit")

print("Proyecto creado correctamente ✔️")
