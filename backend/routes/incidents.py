from flask import Blueprint, jsonify, request
from database import db

from backend.database.models import Incident


incidents_bp = Blueprint("incidents", __name__)

# Get All Incidents
@incidents_bp.route("/api/incidents", methods=["GET"])
def get_incidents():
    incidents = Incident.query.order_by(Incident.timestamp.desc()).all()
    return jsonify([{
        "id": inc.id,
        "description": inc.description,
        "severity": inc.severity,
        "source_ip": inc.source_ip,
        "timestamp": inc.timestamp
    } for inc in incidents])

# Add New Incident
@incidents_bp.route("/api/incidents", methods=["POST"])
def create_incident():
    data = request.json
    new_incident = Incident(
        description=data["description"],
        severity=data["severity"],
        source_ip=data["source_ip"]
    )
    db.session.add(new_incident)
    db.session.commit()
    return jsonify({"message": "Incident created successfully!"}), 201
