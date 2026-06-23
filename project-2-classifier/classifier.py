# Project 2: Data Classification Using AI
# DecodeLabs Internship | Iris KNN Classifier

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, classification_report
import numpy as np

# Step 1: Load dataset
iris = load_iris()
X, y = iris.data, iris.target
print(f"Dataset loaded: {X.shape[0]} samples, {X.shape[1]} features, {len(np.unique(y))} classes")

# Step 2: Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Train-test split (shuffle=True removes order bias)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42, shuffle=True
)
print(f"Train: {len(X_train)} | Test: {len(X_test)}")

# Step 4: Train KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Step 5: Predict + Evaluate
predictions = model.predict(X_test)

cm = confusion_matrix(y_test, predictions)
f1 = f1_score(y_test, predictions, average='weighted')

print("\n--- Confusion Matrix ---")
print(cm)
print(f"\nF1 Score (weighted): {f1:.4f}")
print("\n--- Full Report ---")
print(classification_report(y_test, predictions, target_names=iris.target_names))
