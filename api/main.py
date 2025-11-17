# main.py
from flask import Flask, jsonify
from flask_cors import CORS
from config import DB_URI
from db import db  # importamos la instancia de SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializamos db con la app
db.init_app(app)
CORS(app)

# -------------------------
# Importar blueprints DESPUÉS de inicializar db
# -------------------------
from equipment import equipment_bp
from variables import variables_bp
from measures import measures_bp
from costs import costs_bp
from locations import locations_bp
from equipment_locations import equipment_locations_bp

# Registrar blueprints
app.register_blueprint(equipment_bp)
app.register_blueprint(variables_bp)
app.register_blueprint(measures_bp)
app.register_blueprint(costs_bp)
app.register_blueprint(locations_bp)
app.register_blueprint(equipment_locations_bp)

@app.route("/")
def home():
    return {"message": "H2Lab API running! Created by Pol Pavo"}

# Crear todas las tablas si no existen
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
