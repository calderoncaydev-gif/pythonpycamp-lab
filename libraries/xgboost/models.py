import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def entrenar_modelo(X, y, test_size=0.2, random_state=42):
    """Entrena un modelo de XGBoost y devuelve el modelo y métricas"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    model = xgb.XGBRegressor(n_estimators=100, max_depth=3, learning_rate=0.1)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"MSE del modelo: {mse:.2f}")
    
    return model
