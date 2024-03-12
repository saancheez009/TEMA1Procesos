from flask import Blueprint, Flask

from pelicula.routes import peliculasBP
from actores.routes import actoresBP
from users.routes import usersBP
#from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Registramos los blueprints: primero se indica el nombre
# del Blueprint, en url_prefix indicamos el prefijo de la URL
app.register_blueprint(peliculasBP, url_prefix='/peliculas')
app.register_blueprint(actoresBP, url_prefix='/actores')
app.register_blueprint(usersBP, url_prefix='/users')

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)

#app.config['SECRET_KEY'] = 'tu_clave' # sustituye por una segura
#jwt = JWTManager(app)


#app.config['JSON_AS_ASCII']= False