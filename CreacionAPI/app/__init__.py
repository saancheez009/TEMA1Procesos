
from flask import *

from.periodistas.routes import periodistasBP
from.articulos.routes import articulosBP
from .users.routes import usersBP

from flask import Flask
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave' # sustituye por una segura
jwt = JWTManager(app)


app.config['JSON_AS_ASCII']= False
# Registramos los blueprints: primero se indica el nombre
# del Blueprint, en url_prefix indicamos el prefijo de la URL
app.register_blueprint(periodistasBP, url_prefix='/periodistas')
app.register_blueprint(articulosBP, url_prefix='/articulos')
app.register_blueprint(usersBP, url_prefix='/users')



