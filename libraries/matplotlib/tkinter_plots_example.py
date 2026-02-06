import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from styles import estilo_dark, estilo_light, configurar_titulo, configurar_ejes, activar_grilla

# ======= Función para actualizar el gráfico =======
def actualizar_grafico():
    # Limpiar el eje
    ax.clear()
    
    # Aplicar estilo elegido
    if estilo_var.get() == "Claro":
        estilo_light()
    else:
        estilo_dark()
    
    # Obtener color y tipo de línea
    color = color_var.get()
    linea = linea_var.get()
    
    # Graficar
    ax.plot(x, y, marker='o', color=color, linestyle=linea, label='Datos')
    
    # Configurar gráfico
    configurar_titulo(ax, "Gráfico Interactivo")
    configurar_ejes(ax, "Eje X", "Eje Y")
    activar_grilla(ax)
    ax.legend()
    
    # Actualizar canvas
    canvas.draw()

# ======= Datos de ejemplo =======
x = [1, 2, 3, 4, 5]
y = [2, 5, 7, 3, 6]

# ======= Crear ventana =======
root = tk.Tk()
root.title("Gráfico Interactivo con Tkinter")
root.geometry("700x500")

# ======= Crear figura y eje =======
fig, ax = plt.subplots(figsize=(5,3))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# ======= Variables de selección =======
estilo_var = tk.StringVar(value="Claro")
color_var = tk.StringVar(value="blue")
linea_var = tk.StringVar(value="-")

# ======= Controles de usuario =======
control_frame = ttk.Frame(root)
control_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# Estilo
ttk.Label(control_frame, text="Estilo:").grid(row=0, column=0, padx=5)
ttk.Radiobutton(control_frame, text="Claro", variable=estilo_var, value="Claro", command=actualizar_grafico).grid(row=0, column=1)
ttk.Radiobutton(control_frame, text="Oscuro", variable=estilo_var, value="Oscuro", command=actualizar_grafico).grid(row=0, column=2)

# Color de línea
ttk.Label(control_frame, text="Color:").grid(row=1, column=0, padx=5)
ttk.Combobox(control_frame, textvariable=color_var, values=["blue","red","green","purple","orange"], width=10).grid(row=1, column=1)
color_var.trace("w", lambda *args: actualizar_grafico())

# Tipo de línea
ttk.Label(control_frame, text="Línea:").grid(row=2, column=0, padx=5)
ttk.Combobox(control_frame, textvariable=linea_var, values=["-","--","-.",":"], width=10).grid(row=2, column=1)
linea_var.trace("w", lambda *args: actualizar_grafico())

# ======= Inicializar gráfico =======
actualizar_grafico()

# ======= Ejecutar aplicación =======
root.mainloop()
