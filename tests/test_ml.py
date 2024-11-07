import joblib

def test_ml_prediction():
    model = joblib.load('ml_model/models/incident_classifier.pkl')
    result = model.predict(["Example incident description"])
    assert result is not None
