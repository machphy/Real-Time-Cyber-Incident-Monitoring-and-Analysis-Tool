from flask import Flask, jsonify
from database import db_session, init_db  # ✅ Import Fix

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Cyber Incident Monitoring API Running!"})

# ✅ Start Backend & Init DB
if __name__ == "__main__":
    init_db()  # 🛠️ Initialize Tables
    app.run(debug=True)
