from src.Rutas.UsuarioCRUD import UsuarioCRUD
from src.Rutas.RolCRUD import RolCRUD
from flask_jwt_extended import JWTManager
from src.Rutas.PermisoCRUD import PermisoCRUD
from src.Autenticación.Autenticacion import Autenticacion
from flask_cors import CORS
from src.Database.database import app
from src.WebSockets.Socket import socketio

app.register_blueprint(UsuarioCRUD)
app.register_blueprint(RolCRUD)
app.register_blueprint(PermisoCRUD)
app.register_blueprint(Autenticacion)

app.config['JWT_SECRET_KEY'] = 'T4nn3R0x#' # Reemplaza con una clave secreta real
jwt = JWTManager(app)

# Habilitar CORS para el localhost
CORS(app)
CORS(app, resources={r"/auth/register": {"origins": "http://10.23.12.8:3000"}})
CORS(app, resources={r"/auth/login": {"origins": "http://10.23.12.8:3000"}})

if __name__ == '__main__':
    socketio.run(app, host='10.23.12.8', port=5000)
    print("Ejecutando")
