
from flask import *

from.periodistas.routes import periodistasBP
from.articulos.routes import articulosBP

app = Flask(__name__) 

app.config['JSON_AS_ASCII']= False
# Registramos los blueprints: primero se indica el nombre
# del Blueprint, en url_prefix indicamos el prefijo de la URL
app.register_blueprint(periodistasBP, url_prefix='/periodistas')
app.register_blueprint(articulosBP, url_prefix='/articulos')



