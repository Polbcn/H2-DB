from flask import Blueprint, request, jsonify
from db import db

class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True)
    locacion = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

locations_bp = Blueprint("locations_bp", __name__, url_prefix="/locations")

@locations_bp.route("/", methods=["POST"])
def create_location():
    data = request.json
    loc = Location(**data)
    db.session.add(loc)
    db.session.commit()
    return jsonify({"id": loc.id, "locacion": loc.locacion})

@locations_bp.route("/", methods=["GET"])
def get_all_locations():
    locations = Location.query.all()
    result = [{"id": l.id, "locacion": l.locacion, "description": l.description} for l in locations]
    return jsonify(result)
