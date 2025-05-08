import logging
import threading
import time
import random
import os
from flask import Flask, send_from_directory, jsonify, render_template, request
from flask_cors import CORS
from flask_socketio import SocketIO
from backend.database import db  # ✅ Correct Import
from backend.routes.incidents import incidents_bp  # ✅ Correct Import
from ml.predict import predict_threat  # ✅ New ML Import

# ✅ Initialize Flask App
app = Flask(
    __name__,
    static_folder=os.path.abspath("frontend/static"),
    template_folder=os.path.abspath("frontend")
)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# ✅ Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://cyber_admin:123456789@localhost/cybersecurity"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ✅ Initialize Database
db.init_app(app)
with app.app_context():
    db.create_all()

# ✅ Register Routes
app.register_blueprint(incidents_bp)

# ✅ Redirect /index.html to /
@app.route("/index.html")
def redirect_to_home():
    return serve_dashboard()

# ✅ Serve Dashboard
@app.route("/")
def serve_dashboard():
    return render_template("index.html")

# ✅ Serve Additional Pages (Threat Logs, Reports, Settings)
@app.route("/pages/<page>")
def serve_pages(page):
    allowed_pages = ["threat_logs.html", "reports.html", "settings.html"]
    if page in allowed_pages:
        return render_template(f"pages/{page}")
    return "Page Not Found", 404

# ✅ Serve Static Files (CSS, JS)
@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# ✅ Setup Logging
LOG_FILE = "backend/logs/server.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

@app.route('/api/logs', methods=['GET'])
def get_logs():
    try:
        with open(LOG_FILE, "r") as log_file:
            logs = log_file.readlines()[-20:]
        return jsonify({"logs": logs})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Predict Threat using ML Model
@app.route('/api/predict-log', methods=['POST'])
def predict_log():
    data = request.get_json()

    features = {
        "src_port": data.get("src_port", 0),
        "dst_port": data.get("dst_port", 0),
        "packet_size": data.get("packet_size", 0),
        "protocol": data.get("protocol", 1)
    }

    predicted_type = predict_threat(features)

    alert = {
        "type": predicted_type,
        "severity": "High",  # Optional: You can predict this too
        "source_ip": data.get("src_ip", "0.0.0.0"),
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }

    socketio.emit("new_alert", alert)
    logging.info(f"📡 ML Alert: {alert}")
    return jsonify({"prediction": predicted_type}), 200

# ✅ Fake Alerts (for Testing)
def generate_fake_alert():
    alert_types = ["DDoS Attack", "Malware Detected", "Unauthorized Access", "Brute Force"]
    severities = ["Critical", "High", "Medium", "Low"]
    return {
        "type": random.choice(alert_types),
        "severity": random.choice(severities),
        "source_ip": f"192.168.1.{random.randint(1, 255)}",
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }

def send_alerts():
    while True:
        alert = generate_fake_alert()
        socketio.emit("new_alert", alert)
        logging.info(f"🔔 New Alert: {alert}")
        time.sleep(5)

@app.route('/api/alerts')
def get_alerts():
    return jsonify([generate_fake_alert() for _ in range(5)])

# ✅ Start Background Alert Thread
threading.Thread(target=send_alerts, daemon=True).start()

# ✅ Run Flask with SocketIO
if __name__ == "__main__":
    print("🚀 Starting Flask Server...")
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
