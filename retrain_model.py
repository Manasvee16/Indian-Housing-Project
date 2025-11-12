"""
Retrain model using scikit-learn GradientBoostingRegressor
This replaces CatBoost with a lighter-weight sklearn model for Vercel deployment
"""
import pandas as pd
import numpy as np
import pickle
import os
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Load training and test data
train_data = pd.read_csv('Artifacts/train_data.csv')
test_data = pd.read_csv('Artifacts/test_data.csv')

# Separate features and target
X_train = train_data.iloc[:, :-1]  # All columns except last (medv)
y_train = train_data.iloc[:, -1]   # Last column (medv)

X_test = test_data.iloc[:, :-1]
y_test = test_data.iloc[:, -1]

print("=" * 60)
print("RETRAINING MODEL WITH SCIKIT-LEARN")
print("=" * 60)
print(f"\nTraining data shape: {X_train.shape}")
print(f"Test data shape: {X_test.shape}")
print(f"Features: {list(X_train.columns)}")

# Train preprocessor (StandardScaler)
preprocessor = StandardScaler()
X_train_scaled = preprocessor.fit_transform(X_train)
X_test_scaled = preprocessor.transform(X_test)

print(f"\n✓ Preprocessor fitted on training data")

# Train GradientBoostingRegressor
print("\nTraining GradientBoostingRegressor...")
model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42
)

model.fit(X_train_scaled, y_train)
print("✓ Model trained successfully")

# Evaluate on test set
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nModel Performance on Test Set:")
print(f"  RMSE: {rmse:.4f}")
print(f"  R² Score: {r2:.4f}")

# Save model and preprocessor
model_path = os.path.join('artifacts', 'model.pkl')
preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

with open(model_path, 'wb') as f:
    pickle.dump(model, f)
    
with open(preprocessor_path, 'wb') as f:
    pickle.dump(preprocessor, f)

model_size = os.path.getsize(model_path) / (1024*1024)
preprocessor_size = os.path.getsize(preprocessor_path) / (1024*1024)

print(f"\n✓ Model saved: {model_path}")
print(f"  Size: {model_size:.3f} MB")
print(f"\n✓ Preprocessor saved: {preprocessor_path}")
print(f"  Size: {preprocessor_size:.3f} MB")

print("\n" + "=" * 60)
print("RETRAINING COMPLETE")
print("=" * 60)
