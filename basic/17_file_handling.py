"""
17_file_handling.py
------------------
Lectura y escritura de archivos.
"""

# Escribir un archivo
with open("example.txt", "w") as f:
    f.write("Hola Mundo\n")
    f.write("Segunda línea\n")

# Leer archivo completo
with open("example.txt", "r") as f:
    content = f.read()
print(content)

# Leer línea por línea
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())

# Añadir al archivo
with open("example.txt", "a") as f:
    f.write("Nueva línea añadida\n")
