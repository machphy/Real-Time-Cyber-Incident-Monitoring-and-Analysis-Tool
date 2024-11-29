from flask import Blueprint, request, jsonify
from utils.database import db
from models.user import User  # Create a User model in `models/user.py`

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(**data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201
