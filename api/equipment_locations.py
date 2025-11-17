from flask import Blueprint, request, jsonify
from db import db
from equipment import Equipment
from locations import Location
from datetime import date

class EquipmentLocation(db.Model):
    __tablename__ = "equipment_locations"

    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipment.id", ondelete="CASCADE"), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id", ondelete="CASCADE"), nullable=False)
    installed_date = db.Column(db.Date, default=date.today)
    removed_date = db.Column(db.Date)
    description = db.Column(db.Text)

    equipment = db.relationship("Equipment", backref="equipment_locations")
    location = db.relationship("Location", backref="equipment_locations")

equipment_locations_bp = Blueprint("equipment_locations_bp", __name__, url_prefix="/equipment_locations")

@equipment_locations_bp.route("/", methods=["POST"])
def create_equipment_location():
    data = request.json
    el = EquipmentLocation(**data)
    db.session.add(el)
    db.session.commit()
    return jsonify({"id": el.id})

@equipment_locations_bp.route("/", methods=["GET"])
def get_all_equipment_locations():
    els = EquipmentLocation.query.all()
    result = [{"id": e.id, "equipment_id": e.equipment_id, "location_id": e.location_id} for e in els]
    return jsonify(result)
