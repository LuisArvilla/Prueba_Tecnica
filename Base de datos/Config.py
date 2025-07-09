
import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect('sigec_db.sqlite')
cursor = conn.cursor()

# Crear tabla "pacientes"
cursor.execute('''
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    fecha_nacimiento DATE,
    genero TEXT CHECK (genero IN ('M', 'F', 'Otro')),
    numero_identificacion TEXT UNIQUE NOT NULL
)
''')

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos 'sigec_db' y tabla 'pacientes' creadas exitosamente.")

