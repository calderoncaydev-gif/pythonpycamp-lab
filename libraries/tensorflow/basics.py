"""
basic.py
Ejemplos básicos de TensorFlow y operaciones con tensores.
"""

import tensorflow as tf
import numpy as np

def crear_tensores():
    """
    Crea tensores simples y realiza operaciones básicas.
    """
    a = tf.constant([1, 2, 3])
    b = tf.constant([4, 5, 6])

    suma = tf.add(a, b)
    multiplicacion = tf.multiply(a, b)
    producto_punto = tf.tensordot(a, b, axes=1)

    print("Tensor a:", a.numpy())
    print("Tensor b:", b.numpy())
    print("Suma:", suma.numpy())
    print("Multiplicación:", multiplicacion.numpy())
    print("Producto punto:", producto_punto.numpy())

def ejemplo_lineal():
    """
    Modelo lineal simple: y = x
    """
    X = np.array([0, 1, 2, 3, 4], dtype=float)
    y = np.array([0, 1, 2, 3, 4], dtype=float)

    model = tf.keras.Sequential([
        tf.keras.Input(shape=(1,)),  # mejor forma de definir input
        tf.keras.layers.Dense(units=1)
    ])

    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(X, y, epochs=50, verbose=0)

    entrada = np.array([[10.0]])  # corregido
    prediccion = model.predict(entrada)
    print("Predicción para 10:", prediccion[0][0])


if __name__ == "__main__":
    print("=== Operaciones básicas con tensores ===")
    crear_tensores()

    print("\n=== Ejemplo de modelo lineal ===")
    ejemplo_lineal()
