# Importar las librerías necesarias
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Cargar el dataset load_wine
wine = load_wine()
X = wine.data  # Características químicas
y = wine.target  # Tipo de vino

# Dividir el dataset en datos de entrenamiento y prueba (20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar un modelo de regresión logística
modelo = LogisticRegression(max_iter=10000, random_state=42)
modelo.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = modelo.predict(X_test)

# Calcular y mostrar la precisión del modelo
precision = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {precision}")