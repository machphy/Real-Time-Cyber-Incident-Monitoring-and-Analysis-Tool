from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

with open('../models/classifier.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = pd.DataFrame(data)
    prediction = model.predict(input_data)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
      #flask web page link to UI sectionds according to there needs