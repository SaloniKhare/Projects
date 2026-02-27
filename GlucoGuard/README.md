# 🩺 GlucoGuard  
### Machine Learning Based Diabetes Prediction Web Application

GlucoGuard is a Flask-based web application that predicts the likelihood of diabetes using Machine Learning.  
The system takes user health parameters through an HTML frontend and returns a prediction result in real-time.

---

## 🚀 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early detection can help in timely medical intervention.

GlucoGuard uses a trained machine learning classification model to predict whether a person is diabetic based on medical attributes such as glucose level, BMI, age, etc.

This project combines:

- 🧠 Machine Learning
- 🌐 Flask Backend
- 🎨 HTML Frontend
- 🐍 Python

---

## 🛠 Tech Stack

**Backend**
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Pickle (for model serialization)

**Frontend**
- HTML

---

## 📊 Dataset

The model is trained using the Pima Indians Diabetes Dataset.

### Input Features:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### ⚙️ How It Works

1. User enters medical details in the web form.
2. Flask receives input data.
3. Data is processed and passed to the trained ML model.
4. Model predicts diabetes risk.
5. Result is displayed on the webpage.

### Output:
- 0 → Non-Diabetic  
- 1 → Diabetic 
