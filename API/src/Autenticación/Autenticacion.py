from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from src.Database.database import db
from src.Modelos.Usuario import Usuario
from random import randint



Autenticacion = Blueprint('Auth', __name__)

@Autenticacion.route('/auth/login', methods=['POST'])
def login():
    nombre = request.json.get('nombre', None)
    contrasena = request.json.get('contrasena', None)

    if not nombre or not contrasena:
        return jsonify({'msg': 'Nombre de usuario o contraseña incorrectos'}), 401

    usuario = Usuario.query.filter_by(nombre=nombre).first()

    if not usuario or not check_password_hash(usuario.contrasena, contrasena):
        return jsonify({'msg': 'Usuario o contraseña incorrectos'}), 401

    token_de_acceso = create_access_token(identity=usuario.idusuario)
    return jsonify({'access_token': token_de_acceso, 'usuario':nombre, 'correo': usuario.email}), 200

@Autenticacion.route('/auth/register', methods=['POST'])
def register():
    nombre = request.json.get('nombre', None)
    correo = request.json.get('email', None)
    contrasena = request.json.get('contrasena', None)

    if not nombre or not correo or not contrasena:
        return jsonify({'msg': 'Faltan campos obligatorios'}), 400

    # Generar un idusuario aleatorio y verificar que no exista en la base de datos
    idusuario = randint(1, 1000)
    while Usuario.find_by_id(idusuario) is not None:
        idusuario = randint(1, 1000)

    if Usuario.find_by_email(correo) is not None:
        return jsonify({'msg': 'El correo electrónico ya está registrado'}), 400

    usuario = Usuario(idusuario=idusuario, nombre=nombre, email=correo, contrasena=generate_password_hash(contrasena))
    db.session.add(usuario)
    db.session.commit()

    token_de_acceso = create_access_token(identity=usuario.idusuario)
    return jsonify({'access_token': token_de_acceso, 'usuario':nombre, 'correo':correo}), 200


