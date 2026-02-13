"""
Script para FreeCAD
Crea un muro de 2500 mm de altura usando el entorno Arch/BIM.
Todas las unidades están en milímetros (mm).

Autor: Ejemplo educativo
"""

import FreeCAD as App
import Draft
import Arch

# ==========================================================
# 1️⃣ CREAR DOCUMENTO NUEVO
# ==========================================================

doc = App.newDocument("Proyecto_Muro")

# ==========================================================
# 2️⃣ DEFINIR DIMENSIONES DEL MURO (EN MILÍMETROS)
# ==========================================================

longitud_muro = 10000   # Largo del muro (4000 mm = 4 metros)
altura_muro = 2500     # Altura del muro (2500 mm = 2.5 metros)
espesor_muro = 200     # Espesor del muro (200 mm)

# ==========================================================
# 3️⃣ CREAR LÍNEA BASE DEL MURO
# ==========================================================
# En Arch, los muros se crean a partir de una línea base.
# Esta línea define el largo y dirección del muro.

linea_base = Draft.makeLine(
    App.Vector(0, 0, 0),               # Punto inicial (X,Y,Z)
    App.Vector(longitud_muro, 0, 0)    # Punto final
)

# Recalcular documento para actualizar geometría
doc.recompute()

# ==========================================================
# 4️⃣ CREAR MURO A PARTIR DE LA LÍNEA
# ==========================================================

muro = Arch.makeWall(linea_base)

# Definir propiedades del muro
muro.Height = altura_muro     # Altura en mm
muro.Width = espesor_muro     # Espesor en mm

doc.recompute()

# ==========================================================
# 5️⃣ CÓMO MOVER EL MURO (EXPLICACIÓN)
# ==========================================================
"""
Existen 3 formas principales de mover el muro:

🔹 MÉTODO 1: Cambiar Placement (posición absoluta)

muro.Placement.Base = App.Vector(1000, 2000, 0)

Esto mueve el muro a:
X = 1000 mm
Y = 2000 mm
Z = 0 mm

🔹 MÉTODO 2: Usar Draft.move (movimiento relativo)

Draft.move(muro, App.Vector(500, 0, 0))

Esto mueve el muro 500 mm en el eje X desde su posición actual.

🔹 MÉTODO 3: Desde interfaz gráfica

1. Selecciona el muro.
2. Usa herramienta "Mover".
3. Ingresa distancia en mm.
"""

print("✅ Muro creado correctamente con 2500 mm de altura")
