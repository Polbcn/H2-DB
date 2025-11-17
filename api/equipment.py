from flask import Blueprint, request, jsonify
from db import db

# -------------------------
# MODELO
# -------------------------
class Equipment(db.Model):
    __tablename__ = "equipment"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100))
    serial_number = db.Column(db.String(100))
    installation_date = db.Column(db.Date)
    lifetime_years = db.Column(db.Float)
    description = db.Column(db.Text)

# -------------------------
# BLUEPRINT
# -------------------------
equipment_bp = Blueprint("equipment_bp", __name__, url_prefix="/equipment")

# -------------------------
# RUTAS
# -------------------------
@equipment_bp.route("/", methods=["POST"])
def create_equipment():
    data = request.json
    eq = Equipment(**data)
    db.session.add(eq)
    db.session.commit()
    return jsonify({"id": eq.id, "name": eq.name})

@equipment_bp.route("/", methods=["GET"])
def get_all_equipment():
    equipments = Equipment.query.all()
    result = [{"id": e.id, "name": e.name} for e in equipments]
    return jsonify(result)
