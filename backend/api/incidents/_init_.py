from flask import Blueprint, request, jsonify
from utils.database import db
from models.incident import Incident  # Make sure you create this model

incidents_blueprint = Blueprint('incidents', __name__)

@incidents_blueprint.route('/', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([incident.to_dict() for incident in incidents])

@incidents_blueprint.route('/', methods=['POST'])
def create_incident():
    data = request.get_json()
    new_incident = Incident(**data)
    db.session.add(new_incident)
    db.session.commit()
    return jsonify(new_incident.to_dict()), 201
