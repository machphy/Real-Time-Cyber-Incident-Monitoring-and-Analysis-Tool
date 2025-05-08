import joblib
import os
import numpy as np

# ✅ Correct path to model
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "threat_model.pkl"))



model = joblib.load(MODEL_PATH)

def predict_threat(features):
    try:
        input_vector = np.array([
            features.get("src_port", 0),
            features.get("dst_port", 0),
            features.get("packet_size", 0),
            features.get("protocol", 0)
        ]).reshape(1, -1)

        prediction = model.predict(input_vector)[0]
        return prediction
    except Exception as e:
        return f"Prediction error: {str(e)}"
