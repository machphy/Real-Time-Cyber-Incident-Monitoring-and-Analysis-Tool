from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Define the base directory and model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../models/classifier.pkl')

# Print the model path for debugging
print(f"Loading model from: {MODEL_PATH}")

# Load the model using joblib
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

@app.route('/classify', methods=['POST'])
def classify_incident():
    try:
        data = request.get_json(force=True)
        incident_features = data.get('incident_features', [])

        if not incident_features:
            return jsonify({"error": "No incident features provided"}), 400

        prediction = model.predict([incident_features])[0]

        return jsonify({"classification": prediction})

    except ValueError as ve:
        return jsonify({"error": f"Value error: {str(ve)}"}), 400
    except TypeError as te:
        return jsonify({"error": f"Type error: {str(te)}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
