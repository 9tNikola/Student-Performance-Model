import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
@st.cache_resource
def load_model():
    model = joblib.load('model/student_performance_model.pkl')
    scaler = joblib.load('model/scaler_logreg.pkl')
    return model, scaler

model, scaler = load_model()

# App title
st.title("Student Performance Predictor")

# Input form
with st.form("prediction_form"):
    st.subheader("Enter Student Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        hours_studied = st.slider("Hours Studied", 1, 10, 5)
        previous_scores = st.slider("Previous Scores", 40, 100, 75)
        extracurricular = st.radio("Extracurricular Activities", ["Yes", "No"])
        
    with col2:
        sleep_hours = st.slider("Sleep Hours", 4, 10, 7)
        papers_practiced = st.slider("Sample Papers Practiced", 0, 10, 3)
    
    submitted = st.form_submit_button("Predict Performance")

# When form is submitted
if submitted:
    # Prepare input data
    extracurricular_num = 1 if extracurricular == "Yes" else 0
    study_sleep_interaction = hours_studied * sleep_hours
    practice_score_interaction = papers_practiced * previous_scores
    
    input_data = pd.DataFrame({
        'Hours Studied': [hours_studied],
        'Previous Scores': [previous_scores],
        'Extracurricular Activities': [extracurricular_num],
        'Sleep Hours': [sleep_hours],
        'Sample Question Papers Practiced': [papers_practiced],
        'Study_Sleep_Interaction': [study_sleep_interaction],
        'Practice_PrevScore_Interaction': [practice_score_interaction]
    })
    
    # Scale features and predict
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    prediction_proba = model.predict_proba(input_scaled)
    
    # Display results
    st.subheader("Prediction Result")
    
    if prediction[0] == 1:
        st.success(f"High Performance (Probability: {prediction_proba[0][1]*100:.1f}%)")
    else:
        st.warning(f"Low Performance (Probability: {prediction_proba[0][0]*100:.1f}%)")
    
    # Show simple feature importance
    st.subheader("Main Influencing Factors")
    st.write("- Previous Scores")
    st.write("- Study Hours × Sleep Hours")
    st.write("- Sample Papers Practiced")

# Simple about section
st.markdown("---")
st.write("""
**About this app**: Predicts student performance based on study habits.
Model accuracy: 92%.
""")