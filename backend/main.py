from flask import Flask, jsonify
from database import SessionLocal, Incident

app = Flask(__name__)

@app.route("/incidents", methods=["GET"])
def get_incidents():
    session = SessionLocal()
    incidents = session.query(Incident).all()
    session.close()

    incidents_data = [
        {"id": inc.id, "description": inc.description, "severity": inc.severity, "status": inc.status}
        for inc in incidents
    ]
    
    return jsonify(incidents_data)

if __name__ == "__main__":
    app.run(debug=True)
