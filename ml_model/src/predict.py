import pickle
import os

MODEL_DIR = "../models/"

# Load model & vectorizer
with open(os.path.join(MODEL_DIR, "trained_model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(MODEL_DIR, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

def predict_incident(text):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return "Cyber Incident Detected" if prediction[0] == 1 else "No Cyber Incident"

print(predict_incident("New cyber attack on government database"))
