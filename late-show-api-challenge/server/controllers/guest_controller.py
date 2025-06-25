
from flask import Blueprint, jsonify
from models.guest import Guest

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    result = [{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests]
    return jsonify(result)