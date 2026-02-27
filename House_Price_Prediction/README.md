# 🏠 House Price Prediction (Bengaluru)

This project predicts house prices in Bengaluru using Machine Learning and deploys the model using Flask.

---

## 📂 Project Files

- app.py → Flask web application  
- hpp.py → Data cleaning and preprocessing script  
- model.py → Model training and saving (Ridge Regression)  
- Bengaluru_House_Data.csv → Original dataset  
- Cleaned_data.csv → Processed dataset  
- RidgeModel.pkl → Trained Ridge model  

---

## ⚙️ Project Workflow

### 1️⃣ Data Preprocessing (hpp.py)
- Removes unnecessary columns  
- Handles missing values  
- Converts total_sqft ranges into numeric values  
- Creates bhk feature from size  
- Performs outlier removal  
- Saves cleaned dataset as `Cleaned_data.csv`  

---

### 2️⃣ Model Training (model.py)
- Imports processed data from `hpp.py`  
- Splits data into training and testing sets  
- Applies:
  - OneHotEncoding on location
  - StandardScaler
- Trains a **Ridge Regression** model  
- Saves trained model as `RidgeModel.pkl`  

---

### 3️⃣ Flask Web Application (app.py)

- Loads `Cleaned_data.csv`
- Loads trained model `RidgeModel.pkl`
- Displays available locations
- Takes user inputs:
  - Location
  - BHK
  - Bathrooms
  - Total Square Feet
- Returns predicted price



---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Pickle

---

## ▶️ How to Run

### Step 1: Train Model
### Step 2: Run Flask App

---

## 📊 Model Used

- Ridge Regression
- R² score used for evaluation

---

## 📌 Dataset

Dataset: `Bengaluru_House_Data.csv`  
Contains house features like:
- Location
- Size
- Total Square Feet
- Bathrooms
- Price

---

## 👩‍💻 Author

Saloni Khare


