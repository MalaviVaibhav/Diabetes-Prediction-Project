# 🎯 Diabetes Prediction App with Clean UI

import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl

# Load the model
pipe = pkl.load(open("Diabeties-Prediction.pkl", "rb"))

# Page setup
st.set_page_config(page_title="Diabetes Predictor", layout="wide")

# Main Title & Description
st.markdown("""
    <h1 style='text-align:center; color:#004d66;'>🩺 Diabetes Prediction App</h1>
    <p style='text-align:center; font-size:16px;'>Built using <b>Logistic Regression</b> to assess your diabetes risk.</p>
    <hr style='border: 1px solid #ccc;' />
""", unsafe_allow_html=True)

# Two-column layout
main_col, side_col = st.columns([2.5, 1])

# ---------------------- Sidebar (Input Form) ----------------------
with side_col:
    st.markdown("""
        <div style='padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9;'>
        <h4 style='color:#006666;'>🔧 Enter Your Details</h4>
    """, unsafe_allow_html=True)

    with st.form("diabetes_form"):
        Pregnancies = st.number_input("Pregnancies", min_value=0)
        Glucose = st.number_input("Glucose (min: 70)", min_value=70)
        BloodPressure = st.number_input("Blood Pressure (min: 80)", min_value=80)
        SkinThickness = st.number_input("Skin Thickness (min: 10)", min_value=10)
        Insulin = st.number_input("Insulin (min: 18)", min_value=18)
        BMI = st.number_input("BMI (min: 18.0)", min_value=18.0, step=0.1, format="%.1f")
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, step=0.01, format="%.3f")
        Age = st.number_input("Age", min_value=1)

        predict_btn = st.form_submit_button("🔍 Predict")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- Main Area (Prediction) ----------------------
with main_col:
    if predict_btn:
        with st.spinner("Analyzing your health data..."):
            # Prepare input DataFrame
            data = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                     BMI, DiabetesPedigreeFunction, Age]]
            columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
                       "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
            input_df = pd.DataFrame(data, columns=columns)

            # Display input
            st.markdown("### ✅ Your Input Summary")
            st.dataframe(input_df)

            # Predict
            result = pipe.predict(input_df)

        # Output Result
        st.markdown("### 🎯 Prediction Result")
        if result[0] == 1:
            st.markdown("""
                <div style='background-color:#ffe6e6; padding:20px; border-left:5px solid #cc0000; border-radius:8px;'>
                    <h3 style='color:#cc0000;'>⚠️ You may have Diabetes</h3>
                    <p>Please consult a medical professional for further diagnosis and guidance.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style='background-color:#e6fff2; padding:20px; border-left:5px solid #00994d; border-radius:8px;'>
                    <h3 style='color:#00994d;'>✅ No Diabetes Detected</h3>
                    <p>Your input indicates no signs of diabetes. Keep maintaining a healthy lifestyle!</p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()

# ---------------------- Footer ----------------------
st.markdown("<hr />", unsafe_allow_html=True)
st.caption("📌 This app uses a Logistic Regression model and is intended for educational purposes only.")
