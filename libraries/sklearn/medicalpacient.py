import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1️⃣ Datos de ejemplo (historial médico)
data = pd.DataFrame({
    "Edad": [45, 60, 30, 50],
    "Peso": [70, 80, 60, 75],
    "Presion": [120, 140, 110, 130],
    "Colesterol": [180, 220, 170, 200],
    "Diabetes": [0, 1, 0, 1],
    "Diagnostico": [1, 0, 1, 0]
})

# 2️⃣ Separar features y target
X = data.drop("Diagnostico", axis=1)
y = data["Diagnostico"]

# 3️⃣ Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# 4️⃣ Escalar datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5️⃣ Entrenar modelo
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train_scaled, y_train)

# 6️⃣ Predecir
y_pred = model.predict(X_test_scaled)

# 7️⃣ Evaluar
print("=== Evaluación del modelo ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 8️⃣ Mostrar datos y predicciones de manera dinámica
print("\n=== Predicciones para pacientes de prueba ===")
for i in range(len(X_test)):
    paciente = X_test.iloc[i].to_dict()  # convierte fila a diccionario
    prediccion = y_pred[i]
    print(f"Paciente {i+1}: {paciente} -> Predicción: {'Enfermedad' if prediccion==1 else 'Saludable'}")
