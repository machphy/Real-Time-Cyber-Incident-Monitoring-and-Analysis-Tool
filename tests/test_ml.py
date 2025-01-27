import joblib

def test_ml_prediction():
    model = joblib.load('ml_model/models/incident_classifier.pkl')
    result = model.predict(["incident discription sho"])
    assert result is not None
