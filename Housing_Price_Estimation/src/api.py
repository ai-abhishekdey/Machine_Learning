# src/api.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="Housing Price Prediction API")

MODEL_PATH = "artifacts/model.joblib"
SCALER_PATH = "artifacts/scaler.joblib"
TEST_CSV = "data/test.csv"

SELECTED_COLUMNS = [
    'grade', 'zipcode', 'lat', 'long', 'sqft_living', 'sqft_living15', 
    'sqft_lot', 'sqft_lot15', 'sqft_above', 'sqft_basement',
    'bedrooms', 'bathrooms', 'floors', 'waterfront', 'view',
    'condition', 'yr_built', 'yr_renovated'
]

# Load model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Input schema
class HousingData(BaseModel):
    grade: float
    zipcode: int
    lat: float
    long: float
    sqft_living: float
    sqft_living15: float
    sqft_lot: float
    sqft_lot15: float
    sqft_above: float
    sqft_basement: float
    bedrooms: float
    bathrooms: float
    floors: float
    waterfront: int
    view: int
    condition: int
    yr_built: int
    yr_renovated: int

@app.post("/predict")
def predict(data: HousingData):
    input_data = np.array([[getattr(data, col) for col in SELECTED_COLUMNS]])
    input_data = scaler.transform(input_data)  # Standardize features
    prediction = model.predict(input_data)
    return {"predicted_price": float(prediction[0])}

@app.get("/predict_test")
def predict_test():
    """Optional endpoint: predict on the test.csv dataset for verification"""
    test_df = pd.read_csv(TEST_CSV)
    x_test = test_df[SELECTED_COLUMNS]
    x_test = scaler.transform(x_test)  # Standardize features
    y_pred = model.predict(x_test)
    return {"predicted_prices": y_pred.tolist()}

@app.get("/")
def root():
    return {"message": "Housing Price Prediction API. Use POST /predict"}
