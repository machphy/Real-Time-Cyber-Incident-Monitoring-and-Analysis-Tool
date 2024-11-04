from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
with open('../models/classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)  # Get data from the request
    # Convert the input data to a DataFrame for the model
    input_data = pd.DataFrame(data)
    prediction = model.predict(input_data)  # Use the model to make a prediction
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
