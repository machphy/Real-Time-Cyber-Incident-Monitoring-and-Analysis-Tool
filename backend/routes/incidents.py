from flask import Blueprint, jsonify, request
from backend.database.models import Incident
 # ✅ Correct Import

# Blueprint for incidents
incidents_bp = Blueprint("incidents", __name__, url_prefix="/api/incidents")

# ✅ GET: Fetch Incidents
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

# ✅ POST: Add New Incident
@incidents_bp.route("/", methods=["POST"])
def create_incident():
    data = request.get_json()
    
    if not data or "description" not in data or "severity" not in data or "status" not in data:
        return jsonify({"error": "Invalid request data"}), 400
    
    new_incident = Incident(
        description=data["description"],
        severity=data["severity"],
        status=data["status"]
    )
    
    db.session.add(new_incident)
    db.session.commit()

    return jsonify({"message": "Incident added successfully!"}), 201

# ✅ Test Alert Route
@incidents_bp.route("/test-alert", methods=["GET"])
def test_alert():
    return jsonify({"message": "Test alert triggered!"}), 200
