import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))

st.title("📊 Customer Prediction App")

st.markdown("Enter **Age** and **Estimated Salary** To Predict whether a person is going to buy our product or Not.")

age = st.number_input("Age",min_value=18, max_value=90, step=5)
estimated_salary = st.number_input("Estimated Salary",min_value=10000, max_value=10000000, step=2000)

input_data = np.array([[age, estimated_salary]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    label = "Yes 🟢 Customer will buy the product" if prediction == 1 else "No 🔴 Customer will not buy the product "
    st.markdown(f"**Prediction**: {label}  ")