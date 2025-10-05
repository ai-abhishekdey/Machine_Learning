# src/train.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
from mlflow.tracking import MlflowClient
import joblib
import os

# ----------------------
# Configuration
# ----------------------
DATA_PATH = "data/Housing.csv"
SELECTED_COLUMNS = [
    'grade', 'zipcode', 'lat', 'long', 'sqft_living', 'sqft_living15', 
    'sqft_lot', 'sqft_lot15', 'sqft_above', 'sqft_basement',
    'bedrooms', 'bathrooms', 'floors', 'waterfront', 'view',
    'condition', 'yr_built', 'yr_renovated'
]
MLFLOW_URI = "http://127.0.0.1:5000"
EXPERIMENT_NAME = "Housing_Price_Production"
MODEL_TYPE = "linear_regression"
MODEL_REGISTRY_NAME = "linear_regression_model"

# ----------------------
# Load data
# ----------------------
df = pd.read_csv(DATA_PATH)
X = df[SELECTED_COLUMNS]
y = df["price"]

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Save train/test CSVs
os.makedirs("data", exist_ok=True)
train_df = pd.concat([x_train.reset_index(drop=True), y_train.reset_index(drop=True)], axis=1)
test_df = pd.concat([x_test.reset_index(drop=True), y_test.reset_index(drop=True)], axis=1)
train_df.to_csv("data/train.csv", index=False)
test_df.to_csv("data/test.csv", index=False)
print("✅ Saved train.csv and test.csv in data")

# ----------------------
# Preprocessing (original notebook style)
# ----------------------
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Save scaler
os.makedirs("artifacts", exist_ok=True)
joblib.dump(scaler, "artifacts/scaler.joblib")

# ----------------------
# MLflow setup
# ----------------------
mlflow.set_tracking_uri(MLFLOW_URI)
client = MlflowClient()
mlflow.set_experiment(EXPERIMENT_NAME)
experiment = client.get_experiment_by_name(EXPERIMENT_NAME)
experiment_id = experiment.experiment_id

# Determine next run number
runs = client.search_runs([experiment_id], filter_string=f"tags.model_type='{MODEL_TYPE}'")
next_id = len(runs) + 1

# ----------------------
# Model training
# ----------------------
params = {"fit_intercept": True}
model = LinearRegression(**params)
model.fit(x_train, y_train)

# ----------------------
# Evaluation
# ----------------------
y_pred = model.predict(x_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
metrics = {"rmse": rmse, "r2_score": r2}

print(f"RMSE: {rmse:.4f}, R² Score: {r2:.4f}")

# ----------------------
# MLflow logging
# ----------------------
run_name = f"run{next_id}_linear_regression"
artifact_path = f"linear_regression_{next_id}"

with mlflow.start_run(run_name=run_name) as run:
    mlflow.set_tag("model_type", MODEL_TYPE)
    mlflow.log_params(params)
    mlflow.log_param("selected_columns", SELECTED_COLUMNS)
    mlflow.log_metrics(metrics)
    
    mlflow.sklearn.log_model(
        sk_model=model,
        name=artifact_path,
        registered_model_name=MODEL_REGISTRY_NAME,
        input_example=x_test[:5]
    )

# Save model locally for API
joblib.dump(model, "artifacts/model.joblib")

print(f"✅ {run_name} completed. Run ID: {run.info.run_id}, Artifact path: {artifact_path}")
print(f"✅ Model registered as '{MODEL_REGISTRY_NAME}' in MLflow Model Registry")
