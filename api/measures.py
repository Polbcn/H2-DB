from flask import Blueprint, request, jsonify
from db import db
from variables import Variable
from datetime import datetime

class Measure(db.Model):
    __tablename__ = "measures"

    id = db.Column(db.BigInteger, primary_key=True)
    variable_id = db.Column(db.Integer, db.ForeignKey("variables.id", ondelete="CASCADE"), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    value_min = db.Column(db.Float)
    value_mean = db.Column(db.Float, nullable=False)
    value_max = db.Column(db.Float)

    variable = db.relationship("Variable", backref="measures")

measures_bp = Blueprint("measures_bp", __name__, url_prefix="/measures")

@measures_bp.route("/", methods=["POST"])
def create_measure():
    data = request.json
    m = Measure(**data)
    db.session.add(m)
    db.session.commit()
    return jsonify({"id": m.id})

@measures_bp.route("/", methods=["GET"])
def get_all_measures():
    measures = Measure.query.all()
    result = [{"id": m.id, "value_mean": m.value_mean} for m in measures]
    return jsonify(result)
