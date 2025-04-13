from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 👨‍🏫 Datos de entrenamiento simulados: 
# Cada fila representa una decisión en la ruta
# [tiempo, es_transbordo (0=no, 1=sí), linea (L1=1, L2=2, L3=3, etc)]
X = [
    [5, 0, 1],   # Ir de A a B en L1, sin transbordo → buena decisión
    [10, 0, 2],  # Ir de A a C en L2, sin transbordo → no tan buena
    [8, 1, 1],   # Ir de B a D en L1, con transbordo → buena
    [12, 0, 2],  # Ir de C a F en L2, sin transbordo → no tan buena
    [9, 1, 3],   # Ir de E a G en L3, con transbordo → buena
    [11, 1, 4],  # Ir de E a H en L4, con transbordo → mala
    [4, 0, 4],   # Ir de F a H en L4, sin transbordo → buena
    [5, 0, 1],   # Ir de G a I en L1, sin transbordo → buena
]

# Y = etiquetas (0 = mala decisión, 1 = buena decisión)
y = [1, 0, 1, 0, 1, 0, 1, 1]

# Dividimos los datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entrenamos el modelo
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Probamos con datos nuevos
X_nuevo = [[6, 1, 3]]  # ¿Ir a otra estación con transbordo en L3 es buena idea?
prediccion = clf.predict(X_nuevo)

print("¿Buena decisión?" , "Sí" if prediccion[0] == 1 else "No")

# Evaluamos precisión
y_pred = clf.predict(X_test)
print("Precisión del modelo:", accuracy_score(y_test, y_pred))
