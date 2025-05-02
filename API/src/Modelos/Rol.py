from src.Database.database import db

class Rol(db.Model):
    __tablename__ = 'rol'
    idrol = db.Column(db.Integer, primary_key=True)
    nombrerol = db.Column(db.String(50), nullable=False)
    descripcionrol = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Rol {self.nombrerol}>'