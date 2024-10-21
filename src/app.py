import streamlit as st
import pickle
import os

model_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../models/xgboost_model.pkl')

# Load the trained model once when the app starts
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

#Page configuration for a more stylish look
st.set_page_config(
    page_title="Student Data Performance Prediction",
    page_icon=":book:",
    layout="wide",  # Options: "centered" (default), "wide"
    initial_sidebar_state="expanded",  # Options: "auto", "expanded", "collapsed"
)

#Adding custom CSS
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        color: #212121;
        background-color: #F5F5F5;
    }
    h1 {
        color: #2A4B7A;
        text-align: center;
    }
    h2 {
        color: #4E5B6A;
        "text-align: center;
    }
    /* Custom button style */
        .stButton > button {
            background-color: #FFEB3B;  
            color: #000000;               
            font-size: 16px;            
            padding: 12px 24px;         
            border-radius: 5px;         
            border: none;               
            cursor: pointer;            
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); 
            transition: background-color 0.3s ease; 
            display: block;
            margin-left: auto;
            margin-right: auto;
        }

        /* Button hover effect */
        .stButton > button:hover {
            background-color: #FBC02D;  
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2);
        }

        /* Button focus effect */
        .stButton > button:focus {
            outline: none;
            box-shadow: 0 0 0 4px rgba(72, 175, 79, 0.3); 
        }
    </style>
    """, unsafe_allow_html=True
)
    

#Centered elements using columns
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the weight of columns
with col2:
    # Streamlit App Title
    st.title("Student Data Performance Prediction App")

    st.markdown(
    """
    <h2 style="text-align: center; color: #4E5B6A;">Purpose</h2>
    """, 
    unsafe_allow_html=True
)

    st.markdown("This model predicts a student's exam score based on factors such as hours studied, attendance, previous test scores, and tutoring sessions.")

    val1 = st.number_input("Hours Studied (per week)", min_value=0.0)
    val2 = st.number_input("Attendance (%)", min_value=0.0)
    val3 = st.number_input("Previous Scores (previous test)", min_value=0.0)
    val4 = st.number_input("Tutoring Sessions (per month)", min_value=0.0)

    if st.button("Predict"):
        data = [[val1, val2, val3, val4]]
        
        prediction = str(model.predict(data)[0])
        
        # Show the predicted class with ## for a bigger font.
        st.write(f"## The predicted exam score is: {prediction}")
        if float(prediction) >= 60:
            st.success(f"Congratulations! You passed with a score of {prediction}!")
        else:
            st.error(f"Sorry. You probably need to study more. Your score is {prediction}.")
        