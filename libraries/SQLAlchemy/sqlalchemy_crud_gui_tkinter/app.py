import tkinter as tk
from tkinter import messagebox
from db import engine, Session
from models import Usuario, Base

# Crear BD y sesión
Base.metadata.create_all(engine)
session = Session()

usuario_seleccionado_id = None

# ---------------- UI ----------------
root = tk.Tk()
root.title("CRUD Usuarios - SQLAlchemy")
root.geometry("420x360")

# Inputs
tk.Label(root, text="Nombre").pack()
nombre_entry = tk.Entry(root)
nombre_entry.pack(fill=tk.X, padx=10)

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack(fill=tk.X, padx=10)

# ---------------- FUNCIONES ----------------
def limpiar_inputs():
    global usuario_seleccionado_id
    usuario_seleccionado_id = None
    nombre_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def crear():
    if not nombre_entry.get() or not email_entry.get():
        messagebox.showwarning("Error", "Complete los campos")
        return

    usuario = Usuario(
        nombre=nombre_entry.get(),
        email=email_entry.get()
    )
    session.add(usuario)
    session.commit()
    listar()
    limpiar_inputs()

def listar():
    lista.delete(0, tk.END)
    usuarios = session.query(Usuario).all()
    for u in usuarios:
        lista.insert(tk.END, f"{u.id} - {u.nombre} - {u.email}")

def cargar_datos(event):
    global usuario_seleccionado_id

    if not lista.curselection():
        return

    seleccionado = lista.get(lista.curselection())
    partes = seleccionado.split(" - ")
    usuario_seleccionado_id = int(partes[0])

    usuario = session.query(Usuario).get(usuario_seleccionado_id)

    nombre_entry.delete(0, tk.END)
    nombre_entry.insert(0, usuario.nombre)

    email_entry.delete(0, tk.END)
    email_entry.insert(0, usuario.email)

def actualizar():
    if usuario_seleccionado_id is None:
        messagebox.showwarning("Error", "Seleccione un usuario")
        return

    usuario = session.query(Usuario).get(usuario_seleccionado_id)
    usuario.nombre = nombre_entry.get()
    usuario.email = email_entry.get()

    session.commit()
    listar()
    limpiar_inputs()

def eliminar():
    if not lista.curselection():
        return

    seleccionado = lista.get(lista.curselection())
    user_id = int(seleccionado.split(" - ")[0])

    usuario = session.query(Usuario).get(user_id)
    session.delete(usuario)
    session.commit()
    listar()
    limpiar_inputs()

# ---------------- BOTONES ----------------
tk.Button(root, text="Crear", command=crear).pack(pady=4)
tk.Button(root, text="Actualizar", command=actualizar).pack(pady=4)
tk.Button(root, text="Eliminar", command=eliminar).pack(pady=4)
tk.Button(root, text="Limpiar", command=limpiar_inputs).pack(pady=4)

# ---------------- LISTA ----------------
lista = tk.Listbox(root)
lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
lista.bind("<<ListboxSelect>>", cargar_datos)

listar()
root.mainloop()
