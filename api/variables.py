from flask import Blueprint, request, jsonify
from db import db
from equipment import Equipment

class Variable(db.Model):
    __tablename__ = "variables"

    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey("equipment.id", ondelete="CASCADE"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    unit = db.Column(db.String(20))
    description = db.Column(db.Text)

    equipment = db.relationship("Equipment", backref="variables")

variables_bp = Blueprint("variables_bp", __name__, url_prefix="/variables")

@variables_bp.route("/", methods=["POST"])
def create_variable():
    data = request.json
    var = Variable(**data)
    db.session.add(var)
    db.session.commit()
    return jsonify({"id": var.id, "name": var.name})

@variables_bp.route("/", methods=["GET"])
def get_all_variables():
    variables = Variable.query.all()
    result = [{"id": v.id, "name": v.name} for v in variables]
    return jsonify(result)
