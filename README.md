# PRUEBA TECNICA

## Duracion para el desarrollo del programa  Aproximadamente 100 minutos
## Duracion del periodo de pruebas           Aproximadamente 50 minutos
## Duracion de la creacion de este documento Aproximadamente 120 minutos

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

## 3. Ejecutar el script para crear la base de datos y ejecutar la pagina web:
En caso de que ya haya una base de datos existente el programa utilizara esa
python app.py

## 4 Prueba de la aplicacion
Se ajunta un archivo "sigec_ddb.sqlite" con 3 pacientes para realizar pruebas
En caso de que desee empezar con una base de datos desde 0, simplemente elimine el archivo "sigec_ddb.sqlite" y vuelva a ejecutar el archivo "app.py"

Abra el local host para verificar el funcionamiento el programa mediante el siguiente link
# http://localhost:5000/

## En caso de que no funcione siga los siguientes pasos para verificar la falla

## 5. Asegurarse de que la base de datos se ha creado correctamente antes de ejecutar la aplicación Flask ejecutando el comando:
sqlite3 sigec_db.sqlite

## 6. Verificar la tabla creada ejecutando el comando:
.tables

## 7. Verificar la estructura de la tabla ejecutando el comando:
.schema pacientes

## 8. Si todo está correcto, puedes proceder a probar las rutas de la API con herramientas como Postman o cURL.

## 9. Para probar la API, asegúrate de que el servidor Flask esté corriendo y utiliza las siguientes rutas:
 - GET /pacientes: Para listar todos los pacientes.
 - POST /pacientes: Para crear un nuevo paciente (requiere un JSON con los campos necesarios).
     return jsonify({'id': paciente_id}), 201
     except sqlite3.IntegrityError:
         return jsonify({'error': 'Identificación duplicada o datos inválidos.'}), 409
 - GET /pacientes/<id>: Para obtener un paciente específico por ID.
 - PUT /pacientes/<id>: Para actualizar un paciente específico por ID (requiere un JSON con los campos a actualizar).
 - DELETE /pacientes/<id>: Para eliminar un paciente específico por ID.

## 10. Si todo lo anterior arroja error 
Es probable que haya sido a causa de una mala instalacion de las herramientas Flask o SQLite, pruebe instalar de nuevo

# Funcionamiento del programa:
La pagina web cuenta con un dieño sencillo pero aagrdadble a la vista.
Con un formulario en el que se solicita:
## • Nombre
## • Apellido
## • Fecha de Nacimiento
## • Género
## • Número de Identificación

![image](https://github.com/user-attachments/assets/27a99e75-9f2d-4318-b659-3f21de4c0454)

Y un boton para cargar los datos del paciente, en el apartado fecha el sistema permite que el usuario:
Seleccione su fecha de nacimiento mediante un calendario
Seleccione su genero mediante un menu de opciones
Escriba su ceula y el programa avisa si es una cedula que ya se encuentra en la base de datos 
Adicionalmente en el apartado cedula solo es posible dijitar numeros sino el programa indica que hay un error y no permite el ingreso a la base de datos.
En caso de un error en el registro por datos invalidos o multiples intentos en un solo momento un el programa manda un mensaje y continua su funcionamiento normal.
![image](https://github.com/user-attachments/assets/bea86075-cd3e-4863-9f5a-ab03bba4c77e)

![image](https://github.com/user-attachments/assets/dc79a28c-cd64-4721-a643-9fbadcd2a3da)

Al añadir un paciente se muestra un mensaje y el ID asignado al mismo
![image](https://github.com/user-attachments/assets/4e7a13cd-b4db-497f-8476-7b0b536e2329)


Una seccion para buscar pacientes utilizando ya sea el ID del paciente o el numero de cedula
Al buscar un paciente si este esta en la base de datos te muestra la informacion de este:
![image](https://github.com/user-attachments/assets/50f549e6-f456-4467-943b-6ee9784e769e)

Sino muestra un mensaje diciendo que "No se encontró ningún paciente con el criterio proporcionado."
![image](https://github.com/user-attachments/assets/1467f7b7-aab3-4460-97a2-06796af66225)

En la parte de abajo se puede observar la lista completa de los pacientes registrados en la base de datos
![image](https://github.com/user-attachments/assets/fd35cee6-ce5c-4c8f-8d14-6f941e64d8d9)



