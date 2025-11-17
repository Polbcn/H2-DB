from flask import Blueprint, request, jsonify
from db import db
from equipment import Equipment
from datetime import date

class Cost(db.Model):
    __tablename__ = "costs"

    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipment.id", ondelete="SET NULL"))
    description = db.Column(db.Text)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, default=date.today)

    equipment = db.relationship("Equipment", backref="costs")

costs_bp = Blueprint("costs_bp", __name__, url_prefix="/costs")

@costs_bp.route("/", methods=["POST"])
def create_cost():
    data = request.json
    c = Cost(**data)
    db.session.add(c)
    db.session.commit()
    return jsonify({"id": c.id})

@costs_bp.route("/", methods=["GET"])
def get_all_costs():
    costs = Cost.query.all()
    result = [{"id": c.id, "amount": c.amount} for c in costs]
    return jsonify(result)
