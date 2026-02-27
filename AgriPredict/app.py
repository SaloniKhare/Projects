from flask import Flask, request, jsonify, send_from_directory
import numpy as np
import joblib
import tensorflow as tf
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')
CORS(app)

# ----------- CONFIGURATION -----------
# Update these paths to match your local file locations
MODEL_PATH = 'models/lstm_agri_model.h5'
SCALER_PATH = 'models/price_scaler.save'
LE_MARKET_PATH = 'models/le_market.save'
LE_COMMODITY_PATH = 'models/le_commodity.save'
LE_VARIETY_PATH = 'models/le_variety.save'
LE_GRADE_PATH = 'models/le_grade.save'
DATASET_PATH = 'data/merged_all.csv'

# ----------- LOAD DATA AND MODELS -----------
print("Loading dataset...")
df = pd.read_csv(DATASET_PATH)

print("Loading model and encoders...")
model = tf.keras.models.load_model(MODEL_PATH, compile=False)
scaler = joblib.load(SCALER_PATH)
le_market = joblib.load(LE_MARKET_PATH)
le_commodity = joblib.load(LE_COMMODITY_PATH)
le_variety = joblib.load(LE_VARIETY_PATH)
le_grade = joblib.load(LE_GRADE_PATH)

print("All models loaded successfully!")

# ----------- SERVE FRONTEND -----------
@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# ----------- API: Get all states -----------
@app.route("/states", methods=["GET"])
def get_states():
    states = sorted(df["State"].unique().tolist())
    return jsonify(states)

# ----------- API: Get districts for a state -----------
@app.route("/districts/<state>", methods=["GET"])
def get_districts(state):
    districts = sorted(df[df["State"] == state]["District"].unique().tolist())
    return jsonify(districts)

# ----------- API: Get markets for state+district -----------
@app.route("/markets/<state>/<district>", methods=["GET"])
def get_markets(state, district):
    markets = sorted(df[
        (df["State"] == state) & 
        (df["District"] == district)
    ]["Market"].unique().tolist())
    return jsonify(markets)

# ----------- API: Get commodities for state+district+market -----------
@app.route("/commodities/<state>/<district>/<market>", methods=["GET"])
def get_commodities(state, district, market):
    commodities = sorted(df[
        (df["State"] == state) & 
        (df["District"] == district) & 
        (df["Market"] == market)
    ]["Commodity"].unique().tolist())
    return jsonify(commodities)

# ----------- API: Get grades for commodity -----------
@app.route("/grades/<state>/<district>/<market>/<commodity>", methods=["GET"])
def get_grades(state, district, market, commodity):
    grades = sorted(df[
        (df["State"] == state) & 
        (df["District"] == district) & 
        (df["Market"] == market) &
        (df["Commodity"] == commodity)
    ]["Grade"].unique().tolist())
    return jsonify(grades)

# ----------- API: Get varieties for commodity+grade -----------
@app.route("/varieties/<state>/<district>/<market>/<commodity>/<grade>", methods=["GET"])
def get_varieties(state, district, market, commodity, grade):
    varieties = sorted(df[
        (df["State"] == state) & 
        (df["District"] == district) & 
        (df["Market"] == market) &
        (df["Commodity"] == commodity) &
        (df["Grade"] == grade)
    ]["Variety"].unique().tolist())
    return jsonify(varieties)

# ----------- API: Prediction -----------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        
        market = data["market"]
        commodity = data["commodity"]
        variety = data["variety"]
        grade = data["grade"]

        # Encode categorical features
        market_val = le_market.transform([market])[0]
        commodity_val = le_commodity.transform([commodity])[0]
        variety_val = le_variety.transform([variety])[0]
        grade_val = le_grade.transform([grade])[0]

        seq_len = 30

        # Filter historical data
        filtered = df[
            (df["Market"] == market) &
            (df["Commodity"] == commodity) &
            (df["Variety"] == variety) &
            (df["Grade"] == grade)
        ].sort_values("Arrival_Date")

        prices = filtered["Modal_Price"].tail(seq_len).values

        if len(prices) < seq_len:
            return jsonify({
                "status": "error", 
                "message": f"Not enough historical data for prediction. Found {len(prices)} records, need {seq_len}."
            })

        seq_input = prices.reshape(1, seq_len, 1)
        forecast = []
        last_sequence = seq_input.copy()

        # 7-day forecast loop
        for _ in range(7):
            X_market = np.array([market_val]).reshape(1, 1)
            X_commodity = np.array([commodity_val]).reshape(1, 1)
            X_variety = np.array([variety_val]).reshape(1, 1)
            X_grade = np.array([grade_val]).reshape(1, 1)

            scaled_pred = model.predict([
                last_sequence, 
                X_market, X_commodity, X_variety, X_grade
            ], verbose=0)

            price_pred = scaler.inverse_transform(scaled_pred)[0][0]
            forecast.append(round(float(price_pred), 2))

            # Update sequence (sliding window)
            new_value_scaled = scaled_pred[0][0]
            next_seq = np.append(last_sequence[0, :, 0], new_value_scaled)[-seq_len:]
            last_sequence = next_seq.reshape(1, seq_len, 1)

        return jsonify({
            "status": "success",
            "forecast": forecast
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# ----------- RUN SERVER -----------
if __name__ == "__main__":
    print("\n" + "="*50)
    print("Agricultural Price Predictor - Local Server")
    print("="*50)
    print(f"Open your browser and go to: http://127.0.0.1:5000")
    print("="*50 + "\n")
    app.run(debug=True, host='127.0.0.1', port=5000)
