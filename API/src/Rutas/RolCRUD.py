from flask import Blueprint, request, jsonify
from src.Database.database import db
from src.Modelos.Rol import Rol

RolCRUD = Blueprint('RolCRUD', __name__)


# Obtener todos los usuarios
@RolCRUD.route('/roles', methods=['GET'])
def obtener_roles():
    roles = Rol.query.all()
    resultado = []
    for rol in roles:
        resultado.append({
            'id': rol.idrol,
            'nombre': rol.nombrerol,
            'descripcion': rol.descripcionrol
        })
    return jsonify(resultado)


# Obtener un rol por ID
@RolCRUD.route('/roles/<int:id>', methods=['GET'])
def obtener_rol(id):
    rol = Rol.query.get(id)
    if rol:
        resultado = {
            'id': rol.idrol,
            'nombre': rol.nombrerol,
            'descripcion': rol.descripcionrol
        }
        return jsonify(resultado)
    else:
        return jsonify({'mensaje': 'El rol no existe'})


# Crear un nuevo rol
@RolCRUD.route('/roles', methods=['POST'])
def crear_rol():
    datos = request.json
    rol = Rol(
        idrol=datos['idrol'],
        nombrerol=datos['nombrerol'],
        descripcionrol=datos['descripcionrol']
    )
    db.session.add(rol)
    db.session.commit()
    return jsonify({'mensaje': 'Rol creado correctamente'})


# Actualizar un rol existente
@RolCRUD.route('/roles/<int:id>', methods=['PUT'])
def actualizar_rol(id):
    rol = Rol.query.get(id)
    if rol:
        datos = request.json
        rol.nombrerol = datos['nombrerol']
        rol.descripcionrol = datos['descripcionrol']
        db.session.commit()
        return jsonify({'mensaje': 'Rol actualizado correctamente'})
    else:
        return jsonify({'mensaje': 'El rol no existe'})


# Eliminar un rol existente
@RolCRUD.route('/roles/<int:id>', methods=['DELETE'])
def eliminar_rol(id):
    rol = Rol.query.get(id)
    if rol:
        db.session.delete(rol)
        db.session.commit()
        return jsonify({'mensaje': 'Rol eliminado correctamente'})
    else:
        return jsonify({'mensaje': 'El rol no existe'})
