# app.py
import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="🏠 Housing Price Prediction", layout="centered")
st.title("🏠 Housing Price Prediction App")

st.markdown("""
Predict the price of a house based on its features.
Use the sliders and number inputs on the sidebar to select feature values.
""")

# ----------------------
# Sidebar inputs
# ----------------------
st.sidebar.header("Enter House Features")

API_URL = "http://127.0.0.1:8000/predict"  # FastAPI endpoint

# Feature ranges / suggestions
feature_ranges = {
    "grade": (1, 13, 7),  # typical house grades 1-13, default 7
    "zipcode": (98000, 98199, 98052),
    "lat": (47.0, 47.8, 47.6),
    "long": (-122.5, -121.5, -122.2),
    "sqft_living": (300, 10000, 2000),
    "sqft_living15": (300, 10000, 2000),
    "sqft_lot": (500, 150000, 7000),
    "sqft_lot15": (500, 150000, 7000),
    "sqft_above": (300, 8000, 1500),
    "sqft_basement": (0, 5000, 500),
    "bedrooms": (0, 10, 3),
    "bathrooms": (0, 8, 2),
    "floors": (1, 3, 1),
    "waterfront": (0, 1, 0),
    "view": (0, 4, 0),
    "condition": (1, 5, 3),
    "yr_built": (1900, 2023, 1970),
    "yr_renovated": (0, 2023, 0)
}

input_data = {}

# Create sidebar inputs
for feature, (min_val, max_val, default_val) in feature_ranges.items():
    if feature in ["zipcode", "waterfront", "view", "condition", "floors", "bedrooms"]:
        input_data[feature] = st.sidebar.number_input(
            f"{feature} (suggested: {default_val})",
            min_value=int(min_val),
            max_value=int(max_val),
            value=int(default_val)
        )
    else:
        input_data[feature] = st.sidebar.slider(
            f"{feature} (range: {min_val}-{max_val}, suggested: {default_val})",
            float(min_val),
            float(max_val),
            float(default_val)
        )

# ----------------------
# Predict via FastAPI
# ----------------------
if st.button("Predict Price"):
    try:
        # Send POST request to FastAPI backend
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            predicted_price = response.json()["predicted_price"]
            st.subheader("Predicted House Price")
            st.success(f"${predicted_price:,.2f}")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"❌ Connection Error: Could not reach API at {API_URL}")
        st.error(str(e))
