from flask import Blueprint, jsonify

incidents_bp = Blueprint("incidents", __name__)

# 🔴 TEMP IN-MEMORY STORE (Stage-1)
INCIDENTS = []

def add_incident(incident):
    INCIDENTS.append(incident)

@incidents_bp.route("/api/incidents", methods=["GET"])
def get_incidents():
    return jsonify({
        "count": len(INCIDENTS),
        "incidents": INCIDENTS[-50:]  # last 50
    })

