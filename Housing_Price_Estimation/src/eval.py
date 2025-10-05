# src/eval.py
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import numpy as np

SCALER_PATH = "artifacts/scaler.joblib"
MODEL_PATH = "artifacts/model.joblib"

SELECTED_COLUMNS = [
    'grade', 'zipcode', 'lat', 'long', 'sqft_living', 'sqft_living15', 
    'sqft_lot', 'sqft_lot15', 'sqft_above', 'sqft_basement',
    'bedrooms', 'bathrooms', 'floors', 'waterfront', 'view',
    'condition', 'yr_built', 'yr_renovated'
]

# Load saved test datasets
test_df = pd.read_csv("data/test.csv")
x_test = test_df[SELECTED_COLUMNS]
y_test = test_df["price"]

# Load scaler and model
scaler = joblib.load(SCALER_PATH)
model = joblib.load(MODEL_PATH)

# Standardize features (original style)
x_test = scaler.transform(x_test)

# Predict & evaluate
y_pred = model.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("=====================================")
print(f"✅ Evaluation on Test Set:")
print(f"RMSE: {rmse:.4f}")
print(f"R² Score: {r2:.4f}")
print("=====================================")