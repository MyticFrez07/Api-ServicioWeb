from flask import Blueprint, request, jsonify
from src.Database.database import db
from src.Modelos.Usuario import Usuario

UsuarioCRUD = Blueprint('UsuarioCRUD', __name__)

# Obtener todos los usuarios
@UsuarioCRUD.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    resultado = []
    for usuario in usuarios:
        resultado.append({
            'id': usuario.idusuario,
            'nombre': usuario.nombre,
            'email': usuario.email,
            'direccion': usuario.direccion,
            'telefono': usuario.telefono
        })
    return jsonify(resultado)

# Obtener un usuario por ID
@UsuarioCRUD.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        resultado = {
            'id': usuario.idusuario,
            'nombre': usuario.nombre,
            'email': usuario.email,
            'direccion': usuario.direccion,
            'telefono': usuario.telefono
        }
        return jsonify(resultado)
    else:
        return jsonify({'mensaje': 'El usuario no existe'})

# Crear un nuevo usuario
@UsuarioCRUD.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.json
    usuario = Usuario(
        idusuario= datos['idusuario'],
        nombre=datos['nombre'],
        email=datos['email'],
        contrasena=datos['contrasena'],
        direccion=datos['direccion'],
        telefono=datos['telefono']
    )
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'mensaje': 'Usuario creado correctamente'})

# Actualizar un usuario existente
@UsuarioCRUD.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        datos = request.json
        usuario.nombre = datos['nombre']
        usuario.email = datos['email']
        usuario.contrasena = datos['contrasena']
        usuario.direccion = datos['direccion']
        usuario.telefono = datos['telefono']
        db.session.commit()
        return jsonify({'mensaje': 'Usuario actualizado correctamente'})
    else:
        return jsonify({'mensaje': 'El usuario no existe'})

# Eliminar un usuario existente
@UsuarioCRUD.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'mensaje': 'Usuario eliminado correctamente'})
    else:
        return jsonify({'mensaje': 'El usuario no existe'})
