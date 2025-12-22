import logging
import threading
import time
import random
import os
from flask import Flask, jsonify, render_template, request, send_from_directory
from flask_cors import CORS

# ===============================
# INTERNAL IMPORTS
# ===============================
from backend.database.models import db
from backend.routes.incidents import incidents_bp, add_incident
from ml.predict import predict_threat

# ===============================
# FLASK APP INIT
# ===============================
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    static_folder=os.path.join(BASE_DIR, "frontend/static"),
    template_folder=os.path.join(BASE_DIR, "frontend")
)

CORS(app)

# ===============================
# DATABASE CONFIG
# ===============================
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://cyber_admin:123456789@localhost/cybersecurity"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# ===============================
# LOGGING CONFIG
# ===============================
LOG_FILE = os.path.join(BASE_DIR, "backend/logs/server.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ===============================
# REGISTER ROUTES
# ===============================
app.register_blueprint(incidents_bp)

# ===============================
# DASHBOARD ROUTES
# ===============================
@app.route("/")
def serve_dashboard():
    return render_template("index.html")

@app.route("/index.html")
def redirect_index():
    return serve_dashboard()

@app.route("/pages/<page>")
def serve_pages(page):
    allowed = ["threat_logs.html", "reports.html", "settings.html"]
    if page in allowed:
        return render_template(f"pages/{page}")
    return "Page Not Found", 404

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# ===============================
# API: SERVER LOGS (READ ONLY)
# ===============================
@app.route("/api/logs", methods=["GET"])
def get_logs():
    try:
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()[-20:]
        return jsonify({"logs": logs})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ===============================
# API: ML PREDICTION → INCIDENT
# ===============================
@app.route("/api/predict-log", methods=["POST"])
def predict_log():
    data = request.get_json()

    features = {
        "src_port": data.get("src_port", 0),
        "dst_port": data.get("dst_port", 0),
        "packet_size": data.get("packet_size", 0),
        "protocol": data.get("protocol", 1)
    }

    threat_type = predict_threat(features)

    incident = {
        "type": threat_type,
        "severity": "High",
        "source_ip": data.get("src_ip", "0.0.0.0"),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    add_incident(incident)
    logging.info(f"📡 ML Incident: {incident}")

    return jsonify({"status": "incident_created", "incident": incident}), 200

# ===============================
# BACKGROUND ALERT GENERATOR (STAGE-1)
# ===============================
def generate_fake_incident():
    return {
        "type": random.choice(
            ["DDoS Attack", "Malware Detected", "Unauthorized Access", "Brute Force"]
        ),
        "severity": random.choice(["Critical", "High", "Medium", "Low"]),
        "source_ip": f"192.168.1.{random.randint(1, 254)}",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def incident_generator():
    while True:
        incident = generate_fake_incident()
        add_incident(incident)
        logging.info(f"🔔 New Incident: {incident}")
        time.sleep(5)

# ===============================
# START BACKGROUND THREAD
# ===============================
threading.Thread(target=incident_generator, daemon=True).start()

# ===============================
# MAIN ENTRY POINT
# ===============================
if __name__ == "__main__":
    print("🚀 RCIMAT Backend Starting (Stage-1)...")
    app.run(host="127.0.0.1", port=5000, debug=True)
