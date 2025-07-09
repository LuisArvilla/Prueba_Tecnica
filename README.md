# IPS

## Comandos de instalacion necesarios para ejecutar el código:

## 1. Instalar Flask:
En la terminal, ejecuta el siguiente comando para instalar Flask, que es el framework web utilizado en este proyecto:
pip install flask

## 2. Instalar SQLite3 (generalmente ya está incluido con Python):
Si no tienes SQLite3 instalado, puedes instalarlo escribiendo el siguiente comando en la terminal:
pip install sqlite3

En caso de que lo anterior no funcione dirijase al sitio web 
## https://www.sqlite.org/download.html 
En la sección Precompiled Binaries for Windows,descargue los archivos:
sqlite-tools
sqlite-dll

Asegúrese de seleccionar los archivos de descarga adecuados, ya que para ambos existen versiones de 32 bits (x86) y 64 bits (x64).
Una vez descargados los archivos y descomprimidos, tienes que moverlos a la carpeta system32 para esto abre explordor de archivos y pega la siguiente ruta C:\WINDOWS\system32
Mueve los archivos, te pedira permisos de administrador, acepta y listo

## 3. Ejecutar el script para crear la base de datos:
python Config.py

## 4. Ejecutar la aplicación Flask:
python app.py

##5. Asegurarse de que la base de datos se ha creado correctamente antes de ejecutar la aplicación Flask:
sqlite3 sigec_db.sqlite

##6. Verificar la tabla creada:
.tables

##7. Verificar la estructura de la tabla:
.schema pacientes

##8. Si todo está correcto, puedes proceder a probar las rutas de la API con herramientas como Postman o cURL.

##9. Para probar la API, asegúrate de que el servidor Flask esté corriendo y utiliza las siguientes rutas:
 - GET /pacientes: Para listar todos los pacientes.
 - POST /pacientes: Para crear un nuevo paciente (requiere un JSON con los campos necesarios).
     return jsonify({'id': paciente_id}), 201
     except sqlite3.IntegrityError:
         return jsonify({'error': 'Identificación duplicada o datos inválidos.'}), 409
 - GET /pacientes/<id>: Para obtener un paciente específico por ID.
 - PUT /pacientes/<id>: Para actualizar un paciente específico por ID (requiere un JSON con los campos a actualizar).
 - DELETE /pacientes/<id>: Para eliminar un paciente específico por ID.
