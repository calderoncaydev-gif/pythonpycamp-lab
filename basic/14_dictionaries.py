"""
14_dictionaries.py
------------------
Diccionarios en Python.
"""

# Crear diccionario
user = {
    "name": "Juan",
    "age": 30,
    "active": True
}

# Acceso
print(user["name"])
print(user.get("email", "no existe"))

# Modificar / agregar
user["age"] = 31
user["email"] = "juan@email.com"

# Eliminar
del user["active"]
email = user.pop("email")

# Recorrer
for key, value in user.items():
    print(key, value)

# Keys, values
print(user.keys())
print(user.values())
