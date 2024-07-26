# app.py
from flask import Flask, request, jsonify, render_template
from google.cloud import aiplatform
import os

app = Flask(__name__)

# Set up the AI Platform client
aiplatform.init(project='adta5240f238jel', location='us-central1')
endpoint = aiplatform.Endpoint('projects/adta5240f238jel/locations/us-central1/endpoints/diabetes_model')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    instance = [
        {
            "Pregnancies": int(data['pregnancies']),
            "Glucose": int(data['glucose']),
            "BloodPressure": int(data['bloodpressure']),
            "SkinThickness": int(data['skinthickness']),
            "Insulin": int(data['insulin']),
            "BMI": float(data['bmi']),
            "DiabetesPedigreeFunction": float(data['diabetespedigreefunction']),
            "Age": int(data['age'])
        }
    ]
    
    prediction = endpoint.predict(instances=instance)
    risk = prediction.predictions[0]
    
    return jsonify({'diabetes_risk': float(risk)})

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    instance = [
        {
            "Pregnancies": int(data['pregnancies']),
            "Glucose": int(data['glucose']),
            "BloodPressure": int(data['bloodpressure']),
            "SkinThickness": int(data['skinthickness']),
            "Insulin": int(data['insulin']),
            "BMI": float(data['bmi']),
            "DiabetesPedigreeFunction": float(data['diabetespedigreefunction']),
            "Age": int(data['age'])
        }
    ]
    
    prediction = endpoint.predict(instances=instance)
    risk = prediction.predictions[0]
    
    return render_template('result.html', risk=float(risk))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))