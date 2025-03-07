from flask import Flask, jsonify
from database import Incident, SessionLocal

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Cyber Incident Monitoring API Running!"})

if __name__ == "__main__":
    app.run(debug=True)
