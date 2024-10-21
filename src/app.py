import streamlit as st
import pickle
import os

model_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../models/xgboost_model.pkl')

# Load the trained model once when the app starts
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit App Title
st.title("Student Data Performance Prediction App")

val1 = st.number_input("Hours Studied (per week)", min_value=0.0)
val2 = st.number_input("Attendance (%)", min_value=0.0)
val3 = st.number_input("Previous Scores (previous test)", min_value=0.0)
val4 = st.number_input("Tutoring Sessions (per month)", min_value=0.0)

if st.button("Predict"):
    data = [[val1, val2, val3, val4]]
    
    prediction = str(model.predict(data)[0])
    
    # Show the predicted class
    st.write(f"The predicted exam score is: {prediction}")