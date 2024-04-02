from flask import Flask
from flask_jwt_extended import JWTManager

from pelicula.routes import peliculasBP
from actores.routes import actoresBP
from users.routes import usersBP
import string
import secrets


#contraseña aleatoria
alphabet=string.ascii_letters + string.digits
password=''.join(secrets.choice(alphabet)for i in range(8))

app = Flask(__name__)

# Registramos los blueprints: primero se indica el nombre
# del Blueprint, en url_prefix indicamos el prefijo de la URL
app.register_blueprint(peliculasBP, url_prefix='/peliculas')
app.register_blueprint(actoresBP, url_prefix='/actores')
app.register_blueprint(usersBP, url_prefix='/users')


app.config['SECRET_KEY'] = password
jwt = JWTManager(app)

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
