import logging
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO
from database import db  # ✅ Database Import
from routes.incidents import incidents_bp

# ✅ Flask App Initialization
app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")
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

# ✅ Serve Frontend Files
@app.route("/")
def serve_dashboard():
    return send_from_directory(app.static_folder, "index.html")

# ✅ Setup Logging
logging.basicConfig(filename='backend/logs/server.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/test-log')
def test_log():
    app.logger.info("Test log entry")
    return "Log entry added", 200

# ✅ Run Flask with SocketIO
if __name__ == "__main__":
    print("🚀 Starting Flask Server...")
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)


from flask import Flask, jsonify
from flask_socketio import SocketIO
import threading
import time
import random

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

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
        time.sleep(5)  # Send a new alert every 5 seconds

@app.route('/alerts')
def get_alerts():
    return jsonify([generate_fake_alert() for _ in range(5)])

if __name__ == '__main__':
    threading.Thread(target=send_alerts, daemon=True).start()
    socketio.run(app, debug=True)



from flask import Flask
from routes.incidents import incidents_bp  # Import your routes

app = Flask(__name__)
app.register_blueprint(incidents_bp)  # Make sure this line is present!
