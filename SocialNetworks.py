import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title("📊 My Survey Prediction App")

st.markdown("Enter **Age** and **Estimated Salary** To Predict whether a person is going to buy our product or Not.")

age = st.number_input("Age")
estimated_salary = st.number_input("Estimated Salary")

input_data = np.array([[age, estimated_salary]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    label = "Yes" if prediction == 1 else "No"
    st.markdown(f"**Prediction**: {label} (Raw output: {prediction})")