from flask import Flask, render_template, request, redirect, url_for, session, flash
from modelo import Random_forest
import pandas as pd
import mysql.connector
import bcrypt
import pickle
import qrcode
import os

app = Flask(__name__)
app.secret_key = 'jkSMKnZkaSPn7nrF'  # Cambia esto a una clave secreta segura

# Configuración de la base de datos
db_config = {
    'user': 'admin3',  # Reemplaza con tu usuario de MySQL
    'password': '4nxusOA9@.M1R6F(',  # Reemplaza con tu contraseña de MySQL
    'host': 'localhost',
    'database': 'DB2'  # El nombre de la base de datos que creaste
}

MASTER_KEY = 'CardioNet'

@app.route('/')
def index():
    if 'loggedin' in session:
        return redirect(url_for('home'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'loggedin' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        edad = request.form['edad']
        correo = request.form['correo']
        contra = request.form['contra']
        master = request.form['master']

        if master != MASTER_KEY:
            flash('Clave maestra incorrecta, intente nuevamente') 
            return redirect(url_for('register'))

        # Encriptar la contraseña
        hashed_password = bcrypt.hashpw(contra.encode('utf-8'), bcrypt.gensalt())

        # Conexión a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Insertar el nuevo usuario en la base de datos
        query = "INSERT INTO users (nombres, apellidos, edad, correo, contra) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (nombres, apellidos, edad, correo, hashed_password))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))  # Redirigir al usuario a la página de inicio de sesión

    return render_template('REGISTER.html')

@app.route('/login', methods=['POST'])
def login():
    correo = request.form['correo']
    contra = request.form['contra']

    # Conexión a la base de datos
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Validación del usuario
    query = "SELECT * FROM users WHERE correo = %s"
    cursor.execute(query, (correo,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result and bcrypt.checkpw(contra.encode('utf-8'), result[5].encode('utf-8')):  # result[5] es la columna de la contraseña
        # Crear sesión para el usuario
        session['loggedin'] = True
        session['id'] = result[0]
        session['correo'] = result[4]
        session['nombres'] = result[1]
        session['apellidos'] = result[2]
        return redirect(url_for('home'))  # Redirigir al usuario a la página protegida
    else:
        flash('Correo o contraseña incorrectos')


    return redirect(url_for('index'))

@app.route('/Healthy')
def Healthy():
    if 'loggedin' in session:
        return render_template('Healthy.html')  # Página protegida
    return redirect(url_for('index'))  # Redirigir al usuario a la página de inicio de sesión si no está autenticado


@app.route('/Sick')
def Sick():
    if 'loggedin' in session:
        return render_template('Sick.html')  # Página protegida
    return redirect(url_for('index'))  # Redirigir al usuario a la página de inicio de sesión si no está autenticado

@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html')  # Página protegida
    return redirect(url_for('index'))  # Redirigir al usuario a la página de inicio de sesión si no está autenticado

@app.route('/for_pacientes', methods=['GET', 'POST'])
def for_pacientes():
    if 'loggedin' in session:
        if request.method == 'POST':
            Fullname = request.form['Fullname']
            Edad = int(request.form['Edad'])
            Sexo = int(request.form['Sexo'])
            Tipo_dolor_pecho = int(request.form['Tipo_dolor_pecho'])
            Presion_sanguinea = int(request.form['Presion_sanguinea'])
            Colesterol = int(request.form['Colesterol'])
            Glucosa_en_sangre_mayor_120 = int(request.form['Glucosa_en_sangre_mayor_120'])
            Resultados_EKG = int(request.form['Resultados_EKG'])
            Frecuencia_cardiaca_max = int(request.form['Frecuencia_cardiaca_max'])
            Angina_de_esfuerzo = int(request.form['Angina_de_esfuerzo'])
            Depresion_ST = float(request.form['Depresion_ST'])
            Inclinacion_ST = int(request.form['Inclinacion_ST'])
            Numero_de_vasos_fluor = int(request.form['Numero_de_vasos_fluor'])
            
            # Realizar predicciones
            Enfermedad_cardiaca = Random_forest(Edad, Sexo, Tipo_dolor_pecho, Presion_sanguinea, Colesterol, Glucosa_en_sangre_mayor_120, Resultados_EKG, Frecuencia_cardiaca_max, Angina_de_esfuerzo, Depresion_ST, Inclinacion_ST, Numero_de_vasos_fluor)
            Enfermedad_cardiaca = int(Enfermedad_cardiaca)

            # Conexión a la base de datos
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Insertar datos del paciente en la base de datos
            query = "INSERT INTO pacientes (Fullname, Edad, Sexo, Tipo_dolor_pecho, Presion_sanguinea, Colesterol, Glucosa_en_sangre_mayor_120, Resultados_EKG, Frecuencia_cardiaca_max, Angina_de_esfuerzo, Depresion_ST, Inclinacion_ST, Numero_de_vasos_fluor, Enfermedad_cardiaca) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (Fullname, Edad, Sexo, Tipo_dolor_pecho, Presion_sanguinea, Colesterol, Glucosa_en_sangre_mayor_120, Resultados_EKG, Frecuencia_cardiaca_max, Angina_de_esfuerzo, Depresion_ST, Inclinacion_ST, Numero_de_vasos_fluor, Enfermedad_cardiaca))

            # Obtener el ID del paciente insertado
            paciente_id = cursor.lastrowid

            conn.commit()
            cursor.close()
            conn.close()

            # Generar y guardar QR code
            if Enfermedad_cardiaca == 0:
                qr_page = '/Healthy'
                message = "Paciente sin enfermedad cardiaca"
            elif Enfermedad_cardiaca == 1:
                qr_page = '/Sick'
                message = "Paciente con enfermedad cardiaca"
            
            qr = qrcode.make(request.url_root + qr_page)
            qr_filename = f'static/qrcodes/{paciente_id}.png'  # Nombre del archivo con el ID del paciente
            qr.save(qr_filename)

            # Marcar que se ha generado un QR code
            session['qr_generated'] = True
            session['qr_code_url'] = url_for('static', filename=f'qrcodes/{paciente_id}.png')
            session['qr_message'] = message  # Guardar el mensaje asociado con el QR code

            return redirect(url_for('for_pacientes'))  # Redirigir nuevamente a la página de registro de pacientes

        return render_template('for_pacientes.html', qr_generated=session.get('qr_generated', False), qr_code_url=session.get('qr_code_url', ''), qr_message=session.get('qr_message', ''))  # Mostrar el formulario de registro de pacientes

    return redirect(url_for('index'))  # Redirigir al usuario a la página de inicio de sesión si no está autenticado

@app.route('/logout')
def logout():
    # Eliminar todas las variables de sesión
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('correo', None)
    return redirect(url_for('index'))  # Redirigir al usuario a la página de inicio de sesión después de cerrar sesión

@app.route('/busqueda', methods=['GET', 'POST'])
def busqueda():
    if request.method == 'POST':
        nombre = request.form['nombre']

        # Conexión a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Buscar paciente por nombre
        query = "SELECT * FROM pacientes WHERE Fullname = %s"
        cursor.execute(query, (nombre,))
        paciente = cursor.fetchone()

        cursor.close()
        conn.close()

        if paciente:
            # Si se encuentra al paciente
            paciente_id = paciente[0]
            qr_code_url = url_for('static', filename=f'qrcodes/{paciente_id}.png')
            qr_message = "Paciente encontrado"
            return render_template('busqueda.html', paciente=paciente, qr_code_url=qr_code_url, qr_message=qr_message)
        else:
            # Si no se encuentra al paciente
            flash('Paciente no encontrado')
            return redirect(url_for('busqueda'))

    return render_template('busqueda.html')

@app.route('/config_pacientes', methods=['GET', 'POST'])
def config_pacientes():
    if 'loggedin' in session:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        if request.method == 'POST':
            paciente_id = request.form['paciente_id']
            
            # Eliminar el registro del paciente en la base de datos
            delete_query = "DELETE FROM pacientes WHERE id = %s"
            cursor.execute(delete_query, (paciente_id,))
            
            # Eliminar el archivo QR code asociado
            qr_filename = f'static/qrcodes/{paciente_id}.png'
            if os.path.exists(qr_filename):
                os.remove(qr_filename)
            
            conn.commit()

        # Obtener los datos de los pacientes
        query = "SELECT id, fullname FROM pacientes"
        cursor.execute(query)
        pacientes = cursor.fetchall()

        cursor.close()
        conn.close()

        return render_template('config_pacientes.html', pacientes=pacientes)  # Página protegida
    return redirect(url_for('index'))  # Redirigir al usuario a la página de inicio de sesión si no está autenticado

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)
    