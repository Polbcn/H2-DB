from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

# Crear la app de Flask
app = Flask(__name__)

# Configurar la conexión a la base de datos
DATABASE_URL = "postgres://admin:adminpsswd@db:5432/H2-lab"

# Función para obtener la conexión a la base de datos
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn


@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.json
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        data = request.get_json()
        print(data)
        cur.execute('''
            INSERT INTO consumo (produccion_total, presion_baja, presion_alta, temperatura_exterior, masa_baja, masa_alta, fecha)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (data['produccion_total'], data['presion_baja'], data['presion_alta'], data['temperatura_exterior'],
              data['masa_baja'], data['masa_alta'], data['fecha']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Data added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM consumo ORDER BY fecha DESC')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/get_data_filtered', methods=['GET'])
def get_data_filtered():
    start = request.args.get('start')
    end = request.args.get('end')
    if not start or not end:
        return jsonify({"error": "Provide start and end dates in YYYY-MM-DD format"}), 400
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM consumo WHERE fecha BETWEEN %s AND %s ORDER BY fecha DESC', (start, end))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
