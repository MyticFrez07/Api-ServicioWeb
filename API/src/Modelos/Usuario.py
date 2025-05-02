
from src.Database.database import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    idusuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    contrasena = db.Column(db.String(200), nullable=False)
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    @classmethod
    def find_by_id(cls, idusuario):
        return cls.query.get(idusuario)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'