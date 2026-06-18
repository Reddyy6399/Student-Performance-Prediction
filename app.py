import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Load dataset
data = pd.read_csv("student_exam_scores.csv")

# Features and Target
X = data[['hours_studied',
          'sleep_hours',
          'attendance_percent',
          'previous_scores']]

y = data['exam_score']

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
# SideBar
st.sidebar.header("About")
st.sidebar.write(
    """
    Student Performance Prediction System

    Built using:
    - Python
    - Pandas
    - Scikit-Learn
    - Streamlit
    """
)
# UI
st.title("🎓 Student Performance Predictor")

st.markdown(
    "Predict a student's exam score using Machine Learning."
)
st.divider()
hours = st.number_input("Hours Studied", min_value=0.0)
sleep = st.number_input("Sleep Hours", min_value=0.0)
attendance = st.number_input("Attendance Percentage", min_value=0.0, max_value=100.0)
previous = st.number_input("Previous Score", min_value=0.0)

if st.button("Predict Score"):

    prediction = model.predict(
        [[hours, sleep, attendance, previous]]
    )

    st.success(
        f"Predicted Exam Score: {prediction[0]:.2f}"
    )
    
from sklearn.metrics import r2_score
predictions = model.predict(X_test)
score = r2_score(y_test, predictions)
st.metric("The Model's R² Score", f"{score:.3f}")
