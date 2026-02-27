import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report
app = Flask(__name__)

# Load and prepare data
df = pd.read_csv('diabetes.csv')

X = df.drop(columns='Outcome', axis=1)
Y = df['Outcome']

# Standardize
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Train-test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train model
model = svm.SVC(kernel='linear')
model.fit(X_train, Y_train)
#y_pred_test = model.predict(X_test)
#print("Classification Report:\n", classification_report(Y_test, y_pred_test))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        pregnancies = int(request.form['pregnancies'])
        glucose = int(request.form['glucose'])
        blood_pressure = int(request.form['blood_pressure'])
        skin_thickness = int(request.form['skin_thickness'])
        insulin = int(request.form['insulin'])
        bmi = float(request.form['bmi'])
        diabetes_pedigree_function = float(request.form['diabetes_pedigree_function'])
        age = int(request.form['age'])

        # Make prediction
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)[0]

        # Return result
        if prediction == 0:
            return "The person is not diabetic."
        else:
            return "The person is diabetic."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, port=5500)
