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

# Ruta para obtener todos los sensores
@app.route('/sensores', methods=['GET'])
def get_sensores():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM sensores')
    sensores = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(sensores)

# Ruta para agregar un nuevo sensor
@app.route('/sensores', methods=['POST'])
def add_sensor():
    data = request.get_json()
    nombre_sensor = data['nombre_sensor']
    descripcion_sensor = data.get('descripcion_sensor', '')
    tipo_sensor = data['tipo_sensor']
    ubicacion = data['ubicacion']
    coste = data['coste']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO sensores (nombre_sensor, descripcion_sensor, tipo_sensor, ubicacion, coste)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_sensor;
    ''', (nombre_sensor, descripcion_sensor, tipo_sensor, ubicacion, coste))
    new_sensor_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id_sensor": new_sensor_id}), 201

# Ruta para obtener las mediciones de un sensor específico
@app.route('/mediciones/<int:id_sensor>', methods=['GET'])
def get_mediciones(id_sensor):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('''
        SELECT * FROM mediciones WHERE id_sensor = %s ORDER BY fecha_hora DESC;
    ''', (id_sensor,))
    mediciones = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(mediciones)

# Ruta para agregar una medición
@app.route('/mediciones', methods=['POST'])
def add_medicion():
    data = request.get_json()
    id_sensor = data['id_sensor']
    fecha_hora = data['fecha_hora']
    valor = data['valor']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO mediciones (id_sensor, fecha_hora, valor)
        VALUES (%s, %s, %s)
        RETURNING id_medicion;
    ''', (id_sensor, fecha_hora, valor))
    new_medicion_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id_medicion": new_medicion_id}), 201

# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM usuarios')
    usuarios = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(usuarios)

# Ruta para agregar un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def add_usuario():
    data = request.get_j

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
