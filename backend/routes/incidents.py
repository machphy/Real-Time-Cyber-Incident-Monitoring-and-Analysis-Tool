from flask import Blueprint, jsonify
from database.models import Incident  # ✅ Correct Import
from database import db

# Blueprint for incidents
incidents_bp = Blueprint("incidents", __name__, url_prefix="/api/incidents")

@incidents_bp.route("/", methods=["GET"])
def get_incidents():
    incidents = Incident.query.order_by(Incident.created_at.desc()).all()
    return jsonify([
        {
            "id": i.id,
            "description": i.description,
            "severity": i.severity,
            "status": i.status,
            "created_at": i.created_at
        }
        for i in incidents
    ])


@app.route('/api/test-alert')
def test_alert():
    return jsonify({"message": "Test alert triggered!"}), 200
