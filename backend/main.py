from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Cyber Incident Monitoring API Running!"})

@app.route('/incidents', methods=['GET'])
def get_incidents():
    return jsonify({"incidents": []})  # Abhi empty list return karega

if __name__ == '__main__':
    app.run(debug=True)
