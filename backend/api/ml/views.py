from flask import Blueprint, request, jsonify
import joblib
import os

ml_bp = Blueprint('ml', __name__)
model = joblib.load('ml_model/models/incident_classifier.pkl')

@ml_bp.route('/predict', methods=['POST'])
def predict_incident():
    data = request.get_json()
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction[0]}), 200
