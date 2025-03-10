from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from database import db
from routes.incidents import incidents_bp

app = Flask(__name__)
CORS(app)  # Allow frontend requests
socketio = SocketIO(app, cors_allowed_origins="*")

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://cyber_admin:123456789@localhost/cybersecurity"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Register API Routes
app.register_blueprint(incidents_bp)

@app.route("/")
def home():
    return "✅ Flask API Running!"

if __name__ == "__main__":
    print("🚀 Starting Flask Server...")
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
