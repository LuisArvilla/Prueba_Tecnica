
from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    conn = get_db_connection()
    pacientes = conn.execute('SELECT * FROM pacientes').fetchall()
    conn.close()
    return render_template('index.html', pacientes=pacientes, paciente_encontrado=None)

@app.route('/buscar_paciente')
def buscar_paciente():
    tipo = request.args.get('tipo')
    valor = request.args.get('valor')
    paciente_encontrado = None

    conn = get_db_connection()

    if tipo and valor:
        if tipo == 'id':
            paciente_encontrado = conn.execute(
                'SELECT * FROM pacientes WHERE id = ?',
                (valor,)
            ).fetchone()
        elif tipo == 'cedula':
            paciente_encontrado = conn.execute(
                'SELECT * FROM pacientes WHERE numero_identificacion = ?',
                (valor,)
            ).fetchone()

    pacientes = conn.execute('SELECT * FROM pacientes').fetchall()
    conn.close()

    return render_template('index.html', pacientes=pacientes, paciente_encontrado=paciente_encontrado)

DATABASE = 'sigec_db.sqlite'


# ---------- FUNCIONES DE AYUDA ----------

def get_db_connection():
    conn = sqlite3.connect('sigec_db.sqlite')
    conn.row_factory = sqlite3.Row  # Permite acceder a columnas por nombre
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            fecha_nacimiento DATE,
            genero TEXT CHECK (genero IN ('M', 'F', 'Otro')),
            numero_identificacion TEXT UNIQUE NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Inicializa la base de datos
init_db()

# ---------- RUTAS ----------

# GET /pacientes - Listar todos los pacientes
@app.route('/pacientes', methods=['GET'])
def obtener_pacientes():
    conn = get_db_connection()
    pacientes = conn.execute('SELECT * FROM pacientes').fetchall()
    conn.close()

    return jsonify([dict(p) for p in pacientes]), 200

# POST /pacientes - Crear nuevo paciente
@app.route('/pacientes', methods=['POST'])
def crear_paciente():
    data = request.get_json()

    campos_requeridos = ['nombre', 'apellido', 'fecha_nacimiento', 'genero', 'numero_identificacion']
    if not all(campo in data for campo in campos_requeridos):
        return jsonify({'error': 'Faltan datos obligatorios.'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, genero, numero_identificacion)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            data['nombre'],
            data['apellido'],
            data['fecha_nacimiento'],
            data['genero'],
            data['numero_identificacion']
        ))
        conn.commit()
        paciente_id = cursor.lastrowid
        conn.close()

        data['id'] = paciente_id
        return jsonify(data), 201
    except sqlite3.IntegrityError as e:
        return jsonify({'error': 'Identificación duplicada o datos inválidos.'}), 409

# GET /pacientes/<id> - Obtener paciente por ID
@app.route('/pacientes/<int:id>', methods=['GET'])
def obtener_paciente_por_id(id):
    conn = get_db_connection()
    paciente = conn.execute('SELECT * FROM pacientes WHERE id = ?', (id,)).fetchone()
    conn.close()

    if paciente is None:
        return jsonify({'error': 'Paciente no encontrado'}), 404

    return jsonify(dict(paciente)), 200

# ---------- EJECUCIÓN ----------
if __name__ == '__main__':
    app.run(debug=True)
