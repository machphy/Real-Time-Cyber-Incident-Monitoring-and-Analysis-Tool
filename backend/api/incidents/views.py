from flask import Blueprint, request, jsonify
from utils.database import db

incidents_bp = Blueprint('incidents', __name__)

@incidents_bp.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    
    incident = db.create_incident(data)
    return jsonify(incident), 201

@incidents_bp.route('/incidents', methods=['GET'])
def get_incidents():
 
    incidents = db.get_all_incidents()
    return jsonify(incidents), 200
