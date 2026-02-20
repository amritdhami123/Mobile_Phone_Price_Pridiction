import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

# App title
st.title("Mobile Phone Price Prediction")

# User inputs
ram = st.number_input("RAM (GB)")
storage = st.number_input("Storage (GB)")
battery = st.number_input("Battery (mAh)")

# Predict button
if st.button("Predict Price"):
    features = np.array([[ram, storage, battery]])
    prediction = model.predict(features)
    st.success(f"Predicted Price: {prediction[0]}")
