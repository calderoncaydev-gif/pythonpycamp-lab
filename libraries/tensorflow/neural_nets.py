"""
neural_nets.py
Ejemplos de redes neuronales usando TensorFlow/Keras.
"""

import tensorflow as tf
import numpy as np

def red_neuronal_basica():
    """
    Red neuronal simple para clasificación binaria.
    """
    # Datos de ejemplo: XOR
    X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
    y = np.array([0,1,1,0], dtype=float)

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(4, activation='relu', input_shape=(2,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, y, epochs=200, verbose=0)

    resultados = model.predict(X)
    print("Predicciones para XOR:")
    for i, val in enumerate(resultados):
        print(f"Entrada: {X[i]}, Predicción: {val[0]:.2f}")

def red_neuronal_mnist():
    """
    Red neuronal para clasificación de dígitos MNIST.
    """
    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()

    # Normalizar
    X_train, X_test = X_train / 255.0, X_test / 255.0

    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28,28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=5, verbose=1)

    loss, acc = model.evaluate(X_test, y_test, verbose=0)
    print(f"Precisión en test MNIST: {acc:.2f}")

if __name__ == "__main__":
    print("=== Red neuronal básica (XOR) ===")
    red_neuronal_basica()

    print("\n=== Red neuronal MNIST ===")
    red_neuronal_mnist()
