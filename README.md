##DIABETES PREDICTION APP
========================

##Overview:
---------
This project is a simple web application built using Streamlit. It predicts whether a person is likely to have diabetes based on input medical data. The model used is a Logistic Regression classifier trained on a dataset containing health metrics like glucose, BMI, insulin levels, etc.

##Features:
---------
- User-friendly web interface
- Input form for health parameters
- Instant prediction with visual feedback
- Built with Streamlit 

##Model Details:
--------------
- Algorithm: Logistic Regression
- Trained on numeric medical features
- Outputs a binary prediction: 0 = No Diabetes, 1 = Diabetes

##Required Libraries:
-------------------
- streamlit
- pandas
- numpy
- scikit-learn


##How to Run:
-----------
1. Make sure you have Python 3.7 or above installed.
2. Install required packages using:
   pip install -r requirements.txt

3. Run the app using:
   streamlit run app.py

##Files:
------
- app.py                    : Main Streamlit application
- Diabeties-Prediction.pkl  : Pickled ML model
- EDA.csv                   : Cleaned dataset used for training
- README.txt                : This file


##Note:
-----
This tool is intended for educational purposes only. It is not a substitute for professional medical advice.

##Created By:
-----------
[Vaibhav Malavi]

