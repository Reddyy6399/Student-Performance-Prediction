# 🎓 Student Performance Prediction System

## Project Overview

The Student Performance Prediction System is a Machine Learning project developed to predict a student's exam score based on academic and behavioral factors.

The project uses historical student data to identify patterns and relationships between different factors affecting academic performance.

The final output is a predicted exam score generated using a Linear Regression model and displayed through an interactive Streamlit web application.

---

# Problem Statement

Educational institutions often want to identify student performance trends early.

The objective of this project is to predict a student's exam score using factors such as:

* Hours Studied
* Sleep Hours
* Attendance Percentage
* Previous Scores

This helps in understanding which factors contribute most to academic success.

---

# Dataset Description

The dataset contains information about students and their academic performance.

## Features (Independent Variables)

### Hours Studied

Number of hours spent studying.

### Sleep Hours

Average daily sleep duration.

### Attendance Percentage

Student attendance percentage.

### Previous Scores

Scores obtained in previous examinations.

## Target Variable (Dependent Variable)

### Exam Score

Final examination score that the model predicts.

---

# Machine Learning Type

This is a:

## Supervised Learning Problem

Because:

* Input data is available
* Output data is available
* The model learns from labeled examples

---

# Why Regression?

The target variable is:

Exam Score

Example:

* 75
* 82
* 91

Since these are numerical values, this becomes a:

## Regression Problem

Not a Classification Problem.

---

# Algorithm Used

## Linear Regression

Linear Regression establishes a relationship between input features and the target variable.

The model attempts to learn:

Exam Score =
a(Hours Studied)

* b(Sleep Hours)
* c(Attendance Percentage)
* d(Previous Scores)
* Constant

Where:

* a, b, c, d are coefficients learned during training.

---

# Project Workflow

## Step 1: Data Collection

Load dataset using Pandas.

```python
data = pd.read_csv("Student_Performance.csv")
```

Purpose:

To bring the dataset into Python for analysis.

---

## Step 2: Data Exploration

Methods Used:

```python
data.head()
data.info()
data.describe()
```

Purpose:

* Understand dataset structure
* Check data types
* Understand statistical properties

---

## Step 3: Data Visualization

Scatter Plot:

Hours Studied vs Exam Score

Purpose:

To visually identify relationships between variables.

Observation:

Students who study more generally score higher marks.

---

## Step 4: Correlation Analysis

Method:

```python
data.corr()
```

Purpose:

To identify relationships between variables.

Observation:

Hours Studied showed the strongest positive correlation with Exam Score.

---

## Step 5: Feature Selection

Features:

```python
X = [
Hours Studied,
Sleep Hours,
Attendance Percentage,
Previous Scores
]
```

Target:

```python
y = Exam Score
```

Purpose:

To separate input variables and output variable.

---

## Step 6: Train-Test Split

Method:

```python
train_test_split()
```

Configuration:

* Training Data = 80%
* Testing Data = 20%

Purpose:

To evaluate model performance on unseen data.

---

## Step 7: Model Training

Algorithm:

```python
LinearRegression()
```

Training:

```python
model.fit(X_train, y_train)
```

Purpose:

To learn patterns from the training dataset.

---

## Step 8: Prediction

Method:

```python
model.predict()
```

Purpose:

To estimate exam scores for new students.

Example:

Input:

Hours Studied = 8

Sleep Hours = 7

Attendance = 85

Previous Score = 80

Output:

Predicted Exam Score

---

## Step 9: Model Evaluation

Metric Used:

### R² Score

Formula:

R² measures how well the model explains variations in the target variable.

Project Result:

R² Score = 0.854

Interpretation:

The model explains approximately 85.4% of the variation in exam scores.

Performance Level:

Excellent

---

# Technologies Used

Programming Language:

* Python

Libraries:

* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Streamlit

Development Environment:

* VS Code

Version Control:

* Git
* GitHub

---

# Streamlit Web Application

The trained model is integrated into a Streamlit application.

Users can enter:

* Hours Studied
* Sleep Hours
* Attendance Percentage
* Previous Scores

The application predicts the expected exam score in real time.

---

# Key Learnings

Through this project I learned:

* Data Analysis
* Data Visualization
* Correlation Analysis
* Feature Selection
* Supervised Learning
* Regression
* Linear Regression
* Train-Test Split
* Model Evaluation
* Streamlit Deployment

---

# Author

Barla Manivith Reddy

B.Tech Artificial Intelligence and Machine Learning

Amity University Bengaluru
